"""Build final video with reference style: black bg + green grid + video frame + assets + captions"""
import json, os

assets_dir = "public/assets"
total_dur = 233.7  # Audio duration

# === SCENE DATA ===
# Each scene has: start time, title shown, which asset folder to use, chart type if no asset
scenes = [
    {"start": 0, "end": 7, "title": "出海最大的敌人不是竞争对手", "sub": "政策一夜之间就变卦了", 
     "asset": None, "chart": "shock_warning", "color": "#FF3366"},
    {"start": 7, "end": 14, "title": "李海涛教授", "sub": "长江商学院院长", 
     "asset": "business_meeting", "chart": None, "color": "#FFD700"},
    {"start": 14, "end": 20, "title": "三大风险", "sub": "美国·政策·欧盟", 
     "asset": None, "chart": "three_risks", "color": "#00FF88"},
    {"start": 20, "end": 28, "title": "美国系统性对抗", "sub": "2026年特朗普政府系列操作", 
     "asset": None, "chart": "usa_map_threat", "color": "#FF3366"},
    {"start": 28, "end": 36, "title": "一带一路 · 全球南方", "sub": "委内瑞拉 · 古巴 · 霍尔木兹", 
     "asset": None, "chart": "belt_road_map", "color": "#00FF88"},
    {"start": 36, "end": 50, "title": "70% - 90%", "sub": "霍尔木兹海峡航运量断崖下降", 
     "asset": None, "chart": "data_7090", "color": "#FFD700"},
    {"start": 50, "end": 60, "title": "政策突变", "sub": "一夜之间政策变卦", 
     "asset": None, "chart": "policy_warning", "color": "#FF3366"},
    {"start": 60, "end": 78, "title": "政策突变案例", "sub": "印尼·印度·越南·沙特·非洲", 
     "asset": None, "chart": "five_countries", "color": "#FF3366"},
    {"start": 78, "end": 90, "title": "欧盟潜在风险", "sub": "最大贸易顺差来源 · 关税冲击", 
     "asset": None, "chart": "eu_trade", "color": "#FFD700"},
    {"start": 90, "end": 98, "title": "三大应对之道", "sub": "地缘洞察 · 合规 · 本地化", 
     "asset": None, "chart": "three_solutions", "color": "#00FF88"},
    {"start": 98, "end": 115, "title": "地缘洞察能力", "sub": "不能只算经济账，不算政治账", 
     "asset": None, "chart": "radar_insight", "color": "#FFD700"},
    {"start": 115, "end": 128, "title": "合规能力", "sub": "合规是门票，不是成本", 
     "asset": "legal_docs", "chart": None, "color": "#00FF88"},
    {"start": 128, "end": 145, "title": "本地化执行能力", "sub": "走进去才能走出来", 
     "asset": "business_meeting", "chart": None, "color": "#00FF88"},
    {"start": 145, "end": 170, "title": "走进去才能走出来", "sub": "深入当地 · 扎根当地 · 与当地共赢", 
     "asset": None, "chart": "golden_quote", "color": "#FFD700"},
    {"start": 170, "end": 195, "title": "抓住机遇 · 管控风险", "sub": "出口逆势上扬，风险不断涌现", 
     "asset": "growth_data", "chart": None, "color": "#00FF88"},
    {"start": 195, "end": 234, "title": "抓住机遇 · 管控风险", "sub": "出口逆势上扬", 
     "asset": None, "chart": "growth_chart", "color": "#00FF88"},
]

# HTML generation
html_parts = []
html_parts.append('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1440">
<title>出海风险分析</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    width:1080px; height:1440px; background:#0A0A0F;
    font-family:"Noto Sans SC","PingFang SC",sans-serif;
    overflow:hidden; position:relative; color:#FFF;
  }

  /* Grid background */
  .bg-grid {
    position:absolute; inset:0; z-index:0;
    background-image:
      linear-gradient(rgba(0,255,136,0.08) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,255,136,0.08) 1px, transparent 1px);
    background-size:60px 60px;
  }

  /* Video frame - the main content area with green border */
  .video-frame {
    position:absolute;
    top:80px; left:60px; right:60px;
    height:720px;
    border:2px solid #00FF88;
    border-radius:4px;
    overflow:hidden;
    z-index:10;
    background:#000;
    box-shadow: 0 0 20px rgba(0,255,136,0.1), inset 0 0 20px rgba(0,255,136,0.05);
  }

  .video-frame video, .video-frame .chart-container {
    width:100%; height:100%;
    object-fit:cover;
  }

  .chart-container {
    display:flex; flex-direction:column;
    justify-content:center; align-items:center;
    background:radial-gradient(ellipse at center, #1a1a2e 0%, #0a0a0f 100%);
    padding:60px;
  }

  /* Title above video */
  .title-area {
    position:absolute;
    top:820px; left:60px; right:60px;
    z-index:20; text-align:center;
  }
  .title-main {
    font-size:52px; font-weight:900; line-height:1.2;
    text-shadow: 0 0 40px rgba(0,255,136,0.3);
  }
  .title-sub {
    font-size:32px; font-weight:600; color:#B0B0C0;
    margin-top:12px;
  }

  /* Captions below */
  .captions-area {
    position:absolute;
    bottom:200px; left:60px; right:60px;
    z-index:30; text-align:center;
  }
  .caption-line {
    display:inline-block; font-size:36px; font-weight:700;
    color:#FFF; text-shadow:0 2px 8px rgba(0,0,0,0.9);
    margin:0 4px; opacity:0.4;
  }

  /* Host zone at bottom */
  .host-zone {
    position:absolute; bottom:0; left:0; right:0; height:180px;
    z-index:40;
    background:linear-gradient(to top, rgba(0,0,0,0.8), transparent);
    border-top:1px solid rgba(0,255,136,0.15);
    display:flex; align-items:center; justify-content:center;
    gap:20px;
  }
  .host-avatar {
    width:100px; height:100px; border-radius:50%;
    border:3px solid #00FF88;
    box-shadow:0 0 20px rgba(0,255,136,0.3);
    background:rgba(0,255,136,0.1);
    display:flex; align-items:center; justify-content:center;
    font-size:40px;
  }
  .host-name {
    font-size:28px; font-weight:700; color:#00FF88;
    text-shadow:0 0 10px rgba(0,255,136,0.5);
  }

  /* Scene container */
  .scene { position:absolute; inset:0; opacity:0; pointer-events:none; z-index:5; }
  .scene.active { opacity:1; pointer-events:auto; }
</style>
</head>
<body>
<div class="bg-grid"></div>

<!-- AUDIO -->
<audio id="narration" src="public/口播音频.mp3" preload="auto"></audio>

<!-- VIDEO FRAME -->
<div class="video-frame" id="videoFrame"></div>

<!-- TITLE -->
<div class="title-area" id="titleArea">
  <div class="title-main" id="titleMain"></div>
  <div class="title-sub" id="titleSub"></div>
</div>

<!-- CAPTIONS -->
<div class="captions-area" id="captionsArea"></div>

<!-- HOST ZONE -->
<div class="host-zone">
  <div class="host-avatar">👤</div>
  <div class="host-name">出海风险分析</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script>
const tl = gsap.timeline({ paused:true });
const scenes = ''' + json.dumps(scenes, ensure_ascii=False) + ''';

const frameEl = document.getElementById('videoFrame');
const titleMain = document.getElementById('titleMain');
const titleSub = document.getElementById('titleSub');
const captionsArea = document.getElementById('captionsArea');

// Scene management
scenes.forEach((s, i) => {
  // Show scene at start time
  tl.call(() => {
    titleMain.textContent = s.title;
    titleMain.style.color = s.color;
    titleSub.textContent = s.sub;
    
    // Update video frame content
    if (s.asset) {
      frameEl.innerHTML = `<video src="public/assets/${s.asset}/${s.asset}_1.mp4" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;"></video>`;
    } else if (s.chart) {
      frameEl.innerHTML = renderChart(s.chart, s.color);
    }
  }, null, s.start);
  
  // Animate title entrance
  tl.fromTo(titleMain, {y:20, opacity:0}, {y:0, opacity:1, duration:0.5, ease:'power2.out'}, s.start);
  tl.fromTo(titleSub, {y:15, opacity:0}, {y:0, opacity:1, duration:0.4, ease:'power2.out'}, s.start+0.2);
  
  // Animate title exit
  tl.to(titleMain, {opacity:0, duration:0.3}, s.end-0.3);
  tl.to(titleSub, {opacity:0, duration:0.3}, s.end-0.3);
});

// Chart rendering functions
function renderChart(type, color) {
  switch(type) {
    case 'shock_warning':
      return `<div class="chart-container">
        <svg viewBox="0 0 400 400" style="width:300px;height:300px;">
          <polygon points="200,30 350,330 50,330" fill="none" stroke="#FF3366" stroke-width="8"/>
          <text x="200" y="220" text-anchor="middle" fill="#FF3366" font-size="80" font-weight="900">!</text>
        </svg>
        <div style="font-size:36px;color:#FF3366;font-weight:900;margin-top:20px;">政策一夜变卦</div>
      </div>`;
    case 'three_risks':
      return `<div class="chart-container">
        <div style="display:flex;gap:30px;">
          ${[ ['01','美国','#FF3366'], ['02','政策','#FF3366'], ['03','欧盟','#FFD700'] ].map(c=>`
            <div style="width:200px;height:280px;border:2px solid ${c[2]};border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,255,255,0.03);">
              <div style="font-size:64px;font-weight:900;color:${c[2]};">${c[0]}</div>
              <div style="font-size:28px;color:#FFF;margin-top:16px;">${c[1]}</div>
            </div>
          `).join('')}
        </div>
      </div>`;
    case 'usa_map_threat':
      return `<div class="chart-container">
        <svg viewBox="0 0 500 300" style="width:500px;height:300px;">
          <path d="M100,150 Q150,80 250,100 T400,140 Q430,160 450,140" fill="none" stroke="#FF3366" stroke-width="4"/>
          <circle cx="250" cy="110" r="15" fill="#FF3366" opacity="0.5"/>
          <text x="250" y="85" text-anchor="middle" fill="#FF3366" font-size="28" font-weight="900">美国</text>
          <line x1="250" y1="125" x2="250" y2="220" stroke="#FF3366" stroke-width="2" stroke-dasharray="5,5"/>
          <rect x="170" y="220" width="160" height="60" rx="8" fill="none" stroke="#FF3366" stroke-width="2"/>
          <text x="250" y="258" text-anchor="middle" fill="#FFF" font-size="22">系统性对抗</text>
        </svg>
        <div style="font-size:28px;color:#FF3366;margin-top:20px;">2026年特朗普政府系列操作</div>
      </div>`;
    case 'belt_road_map':
      return `<div class="chart-container">
        <svg viewBox="0 0 600 300" style="width:600px;height:300px;">
          <path d="M100,150 Q200,100 300,130 T500,120 Q550,110 580,140" fill="none" stroke="#00FF88" stroke-width="3"/>
          <circle cx="100" cy="150" r="12" fill="#00FF88"/>
          <text x="100" y="130" text-anchor="middle" fill="#00FF88" font-size="20">中国</text>
          <circle cx="300" cy="130" r="8" fill="#00FF88" opacity="0.6"/>
          <circle cx="500" cy="120" r="8" fill="#00FF88" opacity="0.6"/>
          <text x="300" y="110" text-anchor="middle" fill="#FFF" font-size="18">全球南方</text>
          <text x="500" y="100" text-anchor="middle" fill="#FFF" font-size="18">一带一路</text>
        </svg>
        <div style="font-size:24px;color:#00FF88;margin-top:20px;">委内瑞拉 · 古巴 · 霍尔木兹</div>
      </div>`;
    case 'data_7090':
      return `<div class="chart-container">
        <div style="font-size:140px;font-weight:900;color:#FFD700;text-shadow:0 0 80px rgba(255,215,0,0.4);">70%–90%</div>
        <div style="font-size:36px;color:#FFF;margin-top:20px;">霍尔木兹海峡航运量断崖下降</div>
        <div style="font-size:24px;color:#B0B0C0;margin-top:16px;">全球20%原油运输通道 · 事实性关闭</div>
      </div>`;
    case 'policy_warning':
      return `<div class="chart-container">
        <svg viewBox="0 0 300 300" style="width:250px;height:250px;">
          <polygon points="150,20 270,260 30,260" fill="none" stroke="#FF3366" stroke-width="6"/>
          <text x="150" y="200" text-anchor="middle" fill="#FF3366" font-size="80" font-weight="900">!</text>
        </svg>
        <div style="font-size:40px;color:#FF3366;font-weight:900;margin-top:20px;">政策突变</div>
        <div style="font-size:28px;color:#B0B0C0;margin-top:10px;">一夜之间政策变卦</div>
      </div>`;
    case 'five_countries':
      return `<div class="chart-container">
        <div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:center;max-width:600px;">
          ${[ ['🇮🇩 印尼','税费·配额'], ['🇮🇳 印度','审查·限制'], ['🇻🇳 越南','自主产业'], ['🇸🇦 沙特','本土化'], ['🌍 非洲','查封·暂停'] ].map(c=>`
            <div style="width:180px;height:140px;border:1px solid rgba(255,51,102,0.4);border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,51,102,0.05);">
              <div style="font-size:28px;font-weight:700;color:#FFF;">${c[0]}</div>
              <div style="font-size:18px;color:#FF3366;margin-top:8px;">${c[1]}</div>
            </div>
          `).join('')}
        </div>
      </div>`;
    case 'eu_trade':
      return `<div class="chart-container">
        <svg viewBox="0 0 500 250" style="width:500px;height:250px;">
          <circle cx="100" cy="125" r="40" fill="none" stroke="#00FF88" stroke-width="2"/>
          <text x="100" y="120" text-anchor="middle" fill="#00FF88" font-size="18">中国</text>
          <text x="100" y="140" text-anchor="middle" fill="#00FF88" font-size="14">出口</text>
          <line x1="140" y1="125" x2="320" y2="125" stroke="#FFD700" stroke-width="6" marker-end="url(#arrow)"/>
          <circle cx="400" cy="125" r="40" fill="none" stroke="#FFD700" stroke-width="2"/>
          <text x="400" y="120" text-anchor="middle" fill="#FFD700" font-size="18">欧盟</text>
          <text x="400" y="140" text-anchor="middle" fill="#FFD700" font-size="14">最大顺差</text>
        </svg>
        <div style="font-size:28px;color:#FFD700;margin-top:20px;">欧盟面临关税冲击风险</div>
      </div>`;
    case 'three_solutions':
      return `<div class="chart-container">
        <div style="display:flex;gap:30px;">
          ${[ ['01','地缘洞察','#FFD700'], ['02','合规','#00FF88'], ['03','本地化','#00FF88'] ].map(c=>`
            <div style="width:200px;height:260px;border:2px solid ${c[2]};border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(0,255,136,0.03);">
              <div style="font-size:56px;font-weight:900;color:${c[2]};">${c[0]}</div>
              <div style="font-size:26px;color:#FFF;margin-top:16px;">${c[1]}</div>
            </div>
          `).join('')}
        </div>
      </div>`;
    case 'radar_insight':
      return `<div class="chart-container">
        <svg viewBox="0 0 300 300" style="width:280px;height:280px;">
          <circle cx="150" cy="150" r="120" fill="none" stroke="#FFD700" stroke-width="1" opacity="0.3"/>
          <circle cx="150" cy="150" r="80" fill="none" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <circle cx="150" cy="150" r="40" fill="none" stroke="#FFD700" stroke-width="1" opacity="0.1"/>
          <line x1="150" y1="30" x2="150" y2="270" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <line x1="30" y1="150" x2="270" y2="150" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <line x1="65" y1="65" x2="235" y2="235" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <line x1="65" y1="235" x2="235" y2="65" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
        </svg>
        <div style="font-size:28px;color:#FFD700;margin-top:20px;">不能只算经济账，不算政治账</div>
      </div>`;
    case 'golden_quote':
      return `<div class="chart-container">
        <div style="font-size:80px;font-weight:900;color:#FFD700;text-align:center;text-shadow:0 0 60px rgba(255,215,0,0.4);">"走进去<br>才能走出来"</div>
        <div style="font-size:28px;color:#B0B0C0;margin-top:30px;">深入当地 · 扎根当地 · 与当地共赢</div>
        <div style="font-size:22px;color:#666;margin-top:16px;">— 李海涛教授</div>
      </div>`;
    case 'growth_chart':
      return `<div class="chart-container">
        <svg viewBox="0 0 500 300" style="width:500px;height:300px;">
          <polyline points="30,270 100,240 170,220 240,190 310,160 380,120 450,70" fill="none" stroke="#00FF88" stroke-width="5" stroke-linecap="round"/>
          <circle cx="100" cy="240" r="8" fill="#00FF88"/>
          <circle cx="240" cy="190" r="8" fill="#00FF88"/>
          <circle cx="380" cy="120" r="8" fill="#00FF88"/>
          <circle cx="450" cy="70" r="10" fill="#00FF88"/>
        </svg>
        <div style="font-size:36px;color:#00FF88;font-weight:700;margin-top:20px;">逆势上扬</div>
      </div>`;
    default:
      return `<div class="chart-container"><div style="font-size:48px;color:${color};font-weight:900;">${type}</div></div>`;
  }
}

// Audio
const audio = document.getElementById('narration');
tl.call(() => audio.play(), [], 0);

// Initial setup
titleMain.style.opacity = '0';
titleSub.style.opacity = '0';

window.__timelines = window.__timelines || {};
window.__timelines['main'] = tl;
</script>
</body>
</html>''')

with open('/workspace/demo_video/chuhai-fenxian/index.html', 'w', encoding='utf-8') as f:
    f.write(html_parts[0])

print(f"Generated index.html ({len(html_parts[0])} bytes)")
print(f"Scenes: {len(scenes)}, Duration: {total_dur}s")
