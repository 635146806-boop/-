"""V5: Rich asset-driven video with proper scene mapping"""
import json

scenes = [
    {"start": 0,   "end": 7,   "title": "出海最大的敌人不是竞争对手", "sub": "政策一夜之间就变卦了",
     "asset": None, "img": "public/assets/oil_strait/oil_strait.png", "color": "#FF3366"},
    {"start": 7,   "end": 14,  "title": "李海涛教授", "sub": "长江商学院院长 · 第十二届走出去风险发布会",
     "asset": "public/assets/business_meeting/business_meeting_1.mp4", "img": None, "color": "#FFD700"},
    {"start": 14,  "end": 20,  "title": "三大风险", "sub": "美国系统性对抗 · 政策突变 · 欧盟潜在风险",
     "asset": None, "img": "public/assets/world_map_bg/world_map_bg.png", "color": "#00FF88"},
    {"start": 20,  "end": 28,  "title": "美国系统性对抗", "sub": "2026年特朗普政府系列操作",
     "asset": None, "img": "public/assets/usa_map/usa_map.png", "color": "#FF3366"},
    {"start": 28,  "end": 36,  "title": "一带一路 · 全球南方", "sub": "委内瑞拉 · 古巴 · 霍尔木兹",
     "asset": None, "img": "public/assets/belt_road/belt_road.png", "color": "#00FF88"},
    {"start": 36,  "end": 50,  "title": "70% – 90%", "sub": "霍尔木兹海峡航运量断崖下降",
     "asset": None, "img": "public/assets/oil_strait/oil_strait.png", "color": "#FFD700"},
    {"start": 50,  "end": 60,  "title": "政策突变", "sub": "一夜之间政策变卦",
     "asset": "public/assets/trading_floor/trading_floor_1.mp4", "img": None, "color": "#FF3366"},
    {"start": 60,  "end": 78,  "title": "政策突变案例", "sub": "印尼 · 印度 · 越南 · 沙特 · 非洲",
     "asset": None, "img": "public/assets/five_nations/five_nations.png", "color": "#FF3366"},
    {"start": 78,  "end": 90,  "title": "欧盟潜在风险", "sub": "最大贸易顺差来源 · 关税冲击",
     "asset": None, "img": "public/assets/eu_map/eu_map.png", "color": "#FFD700"},
    {"start": 90,  "end": 98,  "title": "三大应对之道", "sub": "地缘洞察 · 合规能力 · 本地化执行",
     "asset": "public/assets/city_skyline/city_skyline_1.mp4", "img": None, "color": "#00FF88"},
    {"start": 98,  "end": 115, "title": "地缘洞察能力", "sub": "不能只算经济账，不算政治账",
     "asset": None, "img": "public/assets/world_map_bg/world_map_bg.png", "color": "#FFD700"},
    {"start": 115, "end": 128, "title": "合规能力", "sub": "合规是门票，不是成本",
     "asset": None, "img": "public/assets/compliance_gate/compliance_gate.png", "color": "#00FF88"},
    {"start": 128, "end": 145, "title": "本地化执行能力", "sub": "走进去才能走出来",
     "asset": "public/assets/office_work/office_work_1.mp4", "img": None, "color": "#00FF88"},
    {"start": 145, "end": 170, "title": "走进去才能走出来", "sub": "深入当地 · 扎根当地 · 与当地共赢",
     "asset": None, "img": "public/assets/handshake_win/handshake_win.png", "color": "#FFD700"},
    {"start": 170, "end": 195, "title": "抓住机遇 · 管控风险", "sub": "出口逆势上扬，风险不断涌现",
     "asset": "public/assets/trading_floor/trading_floor_2.mp4", "img": None, "color": "#00FF88"},
    {"start": 195, "end": 234, "title": "抓住机遇 · 管控风险", "sub": "逆势上扬",
     "asset": None, "img": "public/assets/growth_arrow/growth_arrow.png", "color": "#00FF88"},
]

html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1440">
<title>出海风险分析</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { width:1080px; height:1440px; background:#0A0A0F; font-family:"Noto Sans SC","PingFang SC",sans-serif; overflow:hidden; position:relative; color:#FFF; }

  .bg-grid { position:absolute; inset:0; z-index:0;
    background-image:linear-gradient(rgba(0,255,136,0.06) 1px, transparent 1px),linear-gradient(90deg, rgba(0,255,136,0.06) 1px, transparent 1px);
    background-size:60px 60px; }

  .video-frame { position:absolute; top:70px; left:50px; right:50px; height:700px;
    border:2px solid #00FF88; border-radius:6px; overflow:hidden; z-index:10; background:#000;
    box-shadow:0 0 30px rgba(0,255,136,0.12), inset 0 0 30px rgba(0,255,136,0.06); }

  .video-frame video, .video-frame img { width:100%; height:100%; object-fit:cover; }

  .title-area { position:absolute; top:790px; left:50px; right:50px; z-index:20; text-align:center; }
  .title-main { font-size:48px; font-weight:900; line-height:1.2; text-shadow:0 0 40px rgba(0,255,136,0.3); }
  .title-sub { font-size:28px; font-weight:600; color:#B0B0C0; margin-top:10px; }

  .captions-area { position:absolute; bottom:210px; left:50px; right:50px; z-index:30; text-align:center; font-size:34px; font-weight:700; color:#FFF; text-shadow:0 2px 8px rgba(0,0,0,0.9); }

  .host-zone { position:absolute; bottom:0; left:0; right:0; height:170px; z-index:40;
    background:linear-gradient(to top, rgba(0,0,0,0.85), transparent);
    border-top:1px solid rgba(0,255,136,0.12);
    display:flex; align-items:center; justify-content:center; gap:16px; }
  .host-avatar { width:90px; height:90px; border-radius:50%; border:3px solid #00FF88;
    box-shadow:0 0 20px rgba(0,255,136,0.3); background:rgba(0,255,136,0.08);
    display:flex; align-items:center; justify-content:center; font-size:36px; }
  .host-name { font-size:24px; font-weight:700; color:#00FF88; }
</style>
</head>
<body>
<div class="bg-grid"></div>

<audio id="narration" src="public/口播音频.mp3" preload="auto"></audio>

<div class="video-frame" id="videoFrame"></div>

<div class="title-area">
  <div class="title-main" id="titleMain"></div>
  <div class="title-sub" id="titleSub"></div>
</div>

<div class="captions-area" id="captionsArea"></div>

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
const captionsEl = document.getElementById('captionsArea');

scenes.forEach((s, i) => {
  // Update content
  tl.call(() => {
    titleMain.textContent = s.title;
    titleMain.style.color = s.color;
    titleSub.textContent = s.sub;
    
    if (s.asset) {
      frameEl.innerHTML = `<video src="${s.asset}" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;"></video>`;
    } else if (s.img) {
      frameEl.innerHTML = `<img src="${s.img}" style="width:100%;height:100%;object-fit:contain;background:radial-gradient(ellipse at center, #1a1a2e 0%, #0a0a0f 100%);">`;
    }
  }, null, s.start);
  
  // Title animation
  tl.fromTo(titleMain, {y:20, opacity:0}, {y:0, opacity:1, duration:0.4, ease:'power2.out'}, s.start);
  tl.fromTo(titleSub, {y:12, opacity:0}, {y:0, opacity:1, duration:0.3, ease:'power2.out'}, s.start+0.15);
  tl.to(titleMain, {opacity:0, duration:0.25}, s.end-0.25);
  tl.to(titleSub, {opacity:0, duration:0.25}, s.end-0.25);
  
  // Caption text
  tl.call(() => { captionsEl.textContent = s.sub; }, null, s.start);
  tl.fromTo(captionsEl, {opacity:0}, {opacity:1, duration:0.3}, s.start);
  tl.to(captionsEl, {opacity:0, duration:0.25}, s.end-0.25);
});

const audio = document.getElementById('narration');
tl.call(() => audio.play(), [], 0);

titleMain.style.opacity = '0';
titleSub.style.opacity = '0';
captionsEl.style.opacity = '0';

window.__timelines = window.__timelines || {};
window.__timelines['main'] = tl;
</script>
</body>
</html>'''

with open('/workspace/demo_video/chuhai-fenxian/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"V5 index.html: {len(html)} bytes, {len(scenes)} scenes")
