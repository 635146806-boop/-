"""
Build a high-quality HyperFrames video with:
- Rich multi-layer animations per scene
- Audio-synced cue points
- Karaoke-style word-by-word captions
- Particle effects, glow, floating elements
- Professional dark-grid financial analysis style
"""

import json

# Full script with timing cues (seconds from audio)
script = [
    {"start": 0, "end": 6.0, "text": "出海最大的敌人不是竞争对手，怕的是你做生意的国家政策一夜之间就变卦了。",
     "scene": "hook", "visual": "金句冲击", "accent": "#00FF88"},
    {"start": 6.0, "end": 12.0, "text": "这是长江商学院院长李海涛教授在第十二届中国企业走出去风险发布会上的原话。",
     "scene": "intro", "visual": "教授引出", "accent": "#FFD700"},
    {"start": 12.0, "end": 17.2, "text": "李教授说，三个风险是：一、美国的系统性对抗；二、当地政府的政策突变；三、欧盟的潜在风险。",
     "scene": "overview", "visual": "三大风险", "accent": "#00FF88"},
    {"start": 17.2, "end": 23.0, "text": "什么是美国的系统性对抗？从2026年年初至今，美国特朗普政府做了一系列操作，给中国企业出海带来巨大挑战。",
     "scene": "risk1", "visual": "美国风险", "accent": "#FF3366"},
    {"start": 23.0, "end": 30.0, "text": "以前美国人可能没有意识到中国一带一路在全球南方的布局，而现在，它充分意识到全球南方的重要性。",
     "scene": "risk1_detail", "visual": "全球南方", "accent": "#00FF88"},
    {"start": 30.0, "end": 40.0, "text": "比如美以冲突，导致承担全球20%原油运输的霍尔木兹海峡陷入事实性关闭，航运量大幅下降70%至90%，直接威胁中国能源供应链安全。",
     "scene": "risk1_impact", "visual": "数据冲击", "accent": "#FFD700"},
    {"start": 40.0, "end": 48.0, "text": "第二个大的风险是当地政府的政策突变。除了美国，很多当地政府的政策变化，也是重要风险。",
     "scene": "risk2", "visual": "政策突变", "accent": "#FF3366"},
    {"start": 48.0, "end": 62.0, "text": "印尼要求青山集团缴纳更多税费、镍矿配额削减；印度对中国企业严格审查；越南发展自主产业；沙特要求本土化；非洲查封中资账户。",
     "scene": "risk2_cases", "visual": "五国案例", "accent": "#FF3366"},
    {"start": 62.0, "end": 72.0, "text": "第三个也是最重大的风险，是欧盟的潜在风险。由于美国对中国加征关税，大量中国商品涌入欧盟，欧盟面临来自中国商品的冲击。",
     "scene": "risk3", "visual": "欧盟风险", "accent": "#FFD700"},
    {"start": 72.0, "end": 78.0, "text": "李教授也例举了三个应对之道，企业必须具备三大能力。",
     "scene": "solution_overview", "visual": "三大应对", "accent": "#00FF88"},
    {"start": 78.0, "end": 90.0, "text": "第一，地缘洞察能力。要敏感地知道地缘政治如何演变，哪些国家对中国友好，哪些存在风险。不能只算经济账，不算政治账。",
     "scene": "solution1", "visual": "地缘洞察", "accent": "#FFD700"},
    {"start": 90.0, "end": 100.0, "text": "第二，合规能力。一定要合法合规经营，适应当地文化和法规。合规不再是成本，而是门票。",
     "scene": "solution2", "visual": "合规能力", "accent": "#00FF88"},
    {"start": 100.0, "end": 112.0, "text": "第三，本地化执行能力。一定要落地，不是派几个人过去就算了。要熟悉当地文化，真正与当地共赢。",
     "scene": "solution3", "visual": "本地化", "accent": "#00FF88"},
    {"start": 112.0, "end": 130.0, "text": "李海涛教授说：走进去才能走出来。不只是卖产品，而是要深入当地，扎根当地，与当地共赢，合法合规。只有真正走进去了，你才能在风险来的时候走出来，站得住脚。",
     "scene": "quote", "visual": "金句收尾", "accent": "#FFD700"},
    {"start": 130.0, "end": 142.0, "text": "过去一年我们的出口是巨大的亮点，逆势上扬，但是未来潜在的风险也在不断涌现。希望大家既能抓住机遇，也能管控好风险。",
     "scene": "cta", "visual": "行动号召", "accent": "#00FF88"},
]

total_duration = script[-1]["end"] + 3  # 3s padding

# Build the HTML
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1440">
<title>出海风险分析</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  
  body {{
    width: 1080px;
    height: 1440px;
    background: #0A0A0F;
    font-family: "Noto Sans SC", "PingFang SC", sans-serif;
    overflow: hidden;
    position: relative;
    color: #FFFFFF;
  }}

  /* === BACKGROUND LAYERS === */
  .bg-grid {{
    position: absolute; inset: 0; z-index: 0;
    background-image:
      linear-gradient(rgba(26,26,46,0.6) 1px, transparent 1px),
      linear-gradient(90deg, rgba(26,26,46,0.6) 1px, transparent 1px);
    background-size: 60px 60px;
  }}
  
  .bg-glow {{
    position: absolute; inset: 0; z-index: 1;
    background: radial-gradient(ellipse at 50% 35%, rgba(0,255,136,0.06) 0%, transparent 60%);
    opacity: 0;
  }}
  
  .bg-particles {{
    position: absolute; inset: 0; z-index: 2;
    pointer-events: none;
  }}

  /* === SCENE CONTAINER === */
  .scene {{
    position: absolute; inset: 0; z-index: 10;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    padding: 100px 80px 240px 80px;
    opacity: 0;
    pointer-events: none;
  }}
  
  .scene.active {{
    opacity: 1;
    pointer-events: auto;
  }}

  /* === TYPOGRAPHY === */
  .hero {{
    font-size: 72px; font-weight: 900; letter-spacing: -2px;
    line-height: 1.15; text-align: center;
    text-shadow: 0 0 60px rgba(0,255,136,0.3);
  }}
  
  .hero-gold {{
    font-size: 72px; font-weight: 900; letter-spacing: -2px;
    line-height: 1.15; text-align: center; color: #FFD700;
    text-shadow: 0 0 60px rgba(255,215,0,0.3);
  }}
  
  .hero-warn {{
    font-size: 80px; font-weight: 900; letter-spacing: -2px;
    line-height: 1.15; text-align: center; color: #FF3366;
    text-shadow: 0 0 60px rgba(255,51,102,0.4);
  }}
  
  .headline {{
    font-size: 48px; font-weight: 700; line-height: 1.3; text-align: center;
    text-shadow: 0 0 30px rgba(255,255,255,0.15);
  }}
  
  .subtitle {{
    font-size: 36px; font-weight: 500; line-height: 1.5; text-align: center;
    color: #B0B0C0; margin-top: 24px;
  }}
  
  .data-gold {{
    font-size: 120px; font-weight: 900; line-height: 1; text-align: center;
    color: #FFD700;
    text-shadow: 0 0 80px rgba(255,215,0,0.4), 0 0 160px rgba(255,215,0,0.2);
  }}
  
  .data-warn {{
    font-size: 96px; font-weight: 900; line-height: 1; text-align: center;
    color: #FF3366;
    text-shadow: 0 0 60px rgba(255,51,102,0.5);
  }}

  /* === CARDS === */
  .card-row {{
    display: flex; gap: 24px; justify-content: center; width: 100%;
    margin-top: 32px;
  }}
  
  .card {{
    width: 260px; padding: 32px 20px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    text-align: center;
    backdrop-filter: blur(10px);
  }}
  
  .card .num {{
    font-size: 56px; font-weight: 900; line-height: 1;
    margin-bottom: 12px;
  }}
  
  .card .label {{
    font-size: 22px; font-weight: 600; line-height: 1.4;
    color: #B0B0C0;
  }}

  /* === CAPTIONS === */
  .captions {{
    position: absolute; bottom: 160px; left: 80px; right: 80px;
    z-index: 100; text-align: center;
    opacity: 0;
  }}
  
  .caption-word {{
    display: inline-block;
    font-size: 40px; font-weight: 700;
    color: #FFFFFF;
    text-shadow: 0 2px 8px rgba(0,0,0,0.8), 0 0 20px rgba(0,0,0,0.5);
    margin: 0 6px;
    opacity: 0.3;
    transition: none;
  }}
  
  .caption-word.active {{
    opacity: 1;
    color: #00FF88;
    text-shadow: 0 0 30px rgba(0,255,136,0.5), 0 2px 8px rgba(0,0,0,0.8);
  }}

  /* === HOST ZONE === */
  .host-zone {{
    position: absolute; bottom: 0; left: 0; right: 0; height: 140px;
    z-index: 50;
    background: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
    border-top: 1px solid rgba(0,255,136,0.1);
  }}

  /* === PARTICLES === */
  .particle {{
    position: absolute;
    border-radius: 50%;
    pointer-events: none;
  }}

  /* === GLOW ORB === */
  .glow-orb {{
    position: absolute; border-radius: 50%;
    filter: blur(80px);
    pointer-events: none;
  }}
</style>
</head>
<body>

<div class="bg-grid"></div>
<div class="bg-glow"></div>
<div class="bg-particles" id="particles"></div>

<!-- === SCENES === -->
'''

# Generate scenes
scene_data = {
    "hook": {
        "title_class": "hero-warn",
        "title": "政策一夜变卦",
        "subtitle": "出海最大的敌人不是竞争对手",
        "accent": "#FF3366",
    },
    "intro": {
        "title_class": "hero-gold",
        "title": "李海涛教授",
        "subtitle": "长江商学院院长 · 第十二届走出去风险发布会",
        "accent": "#FFD700",
    },
    "overview": {
        "title_class": "headline",
        "title": "三大风险",
        "subtitle": "",
        "accent": "#00FF88",
        "cards": [
            {"num": "01", "label": "美国\n系统性对抗", "color": "#FF3366"},
            {"num": "02", "label": "当地政府\n政策突变", "color": "#FF3366"},
            {"num": "03", "label": "欧盟\n潜在风险", "color": "#FFD700"},
        ]
    },
    "risk1": {
        "title_class": "hero-warn",
        "title": "美国系统性对抗",
        "subtitle": "2026年特朗普政府系列操作",
        "accent": "#FF3366",
    },
    "risk1_detail": {
        "title_class": "headline",
        "title": "全球南方",
        "subtitle": "一带一路布局 · 委内瑞拉 · 古巴 · 霍尔木兹",
        "accent": "#00FF88",
    },
    "risk1_impact": {
        "title_class": "data-gold",
        "title": "70% – 90%",
        "subtitle": "霍尔木兹海峡航运量断崖下降",
        "accent": "#FFD700",
    },
    "risk2": {
        "title_class": "hero-warn",
        "title": "政策突变",
        "subtitle": "一夜之间政策变卦",
        "accent": "#FF3366",
    },
    "risk2_cases": {
        "title_class": "headline",
        "title": "政策突变案例",
        "subtitle": "",
        "accent": "#FF3366",
        "cards": [
            {"num": "🇮🇩", "label": "印尼\n税费·配额"},
            {"num": "🇮🇳", "label": "印度\n审查·限制"},
            {"num": "🇻🇳", "label": "越南\n自主产业"},
            {"num": "🇸🇦", "label": "沙特\n本土化"},
            {"num": "🌍", "label": "非洲\n查封·暂停"},
        ]
    },
    "risk3": {
        "title_class": "hero",
        "title": "欧盟潜在风险",
        "subtitle": "最大贸易顺差来源 · 关税冲击",
        "accent": "#FFD700",
    },
    "solution_overview": {
        "title_class": "headline",
        "title": "三大应对之道",
        "subtitle": "",
        "accent": "#00FF88",
        "cards": [
            {"num": "01", "label": "地缘洞察\n能力", "color": "#FFD700"},
            {"num": "02", "label": "合规\n能力", "color": "#00FF88"},
            {"num": "03", "label": "本地化执行\n能力", "color": "#00FF88"},
        ]
    },
    "solution1": {
        "title_class": "hero-gold",
        "title": "地缘洞察能力",
        "subtitle": "不能只算经济账，不算政治账",
        "accent": "#FFD700",
    },
    "solution2": {
        "title_class": "hero",
        "title": "合规能力",
        "subtitle": "合规是门票，不是成本",
        "accent": "#00FF88",
    },
    "solution3": {
        "title_class": "hero",
        "title": "本地化执行能力",
        "subtitle": "走进去才能走出来",
        "accent": "#00FF88",
    },
    "quote": {
        "title_class": "hero-gold",
        "title": "走进去才能走出来",
        "subtitle": "深入当地 · 扎根当地 · 与当地共赢",
        "accent": "#FFD700",
    },
    "cta": {
        "title_class": "hero",
        "title": "抓住机遇 · 管控风险",
        "subtitle": "出口逆势上扬，风险不断涌现",
        "accent": "#00FF88",
    },
}

for seg in script:
    sid = seg["scene"]
    sd = scene_data.get(sid, {})
    title = sd.get("title", "")
    subtitle = sd.get("subtitle", "")
    title_class = sd.get("title_class", "headline")
    cards = sd.get("cards", [])
    
    cards_html = ""
    if cards:
        cards_html = '<div class="card-row">'
        for c in cards:
            color = c.get("color", "#00FF88")
            cards_html += f'<div class="card"><div class="num" style="color:{color}">{c["num"]}</div><div class="label">{c["label"]}</div></div>'
        cards_html += '</div>'
    
    html += f'''
  <div class="scene" id="scene-{sid}">
    <div class="{title_class}">{title}</div>
    {f'<div class="subtitle">{subtitle}</div>' if subtitle else ''}
    {cards_html}
  </div>
'''

html += f'''
  <!-- Captions -->
  <div class="captions" id="captions"></div>
  
  <!-- Host zone placeholder -->
  <div class="host-zone"></div>

  <!-- Audio -->
  <audio id="narration" src="public/口播音频.mp3" preload="auto"></audio>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    const totalDuration = {total_duration};
    
    // ===== PARTICLE SYSTEM =====
    const particlesEl = document.getElementById('particles');
    const particles = [];
    const PARTICLE_COUNT = 30;
    
    for (let i = 0; i < PARTICLE_COUNT; i++) {{
      const p = document.createElement('div');
      p.className = 'particle';
      const size = 2 + Math.random() * 4;
      p.style.width = size + 'px';
      p.style.height = size + 'px';
      p.style.background = Math.random() > 0.7 ? '#00FF88' : 'rgba(255,255,255,0.3)';
      p.style.left = Math.random() * 1080 + 'px';
      p.style.top = Math.random() * 1440 + 'px';
      p.style.opacity = 0;
      particlesEl.appendChild(p);
      particles.push(p);
    }}
    
    // Particle drift animation
    particles.forEach((p, i) => {{
      tl.to(p, {{
        x: () => (Math.random() - 0.5) * 200,
        y: () => (Math.random() - 0.5) * 300,
        opacity: () => 0.1 + Math.random() * 0.3,
        duration: 8 + Math.random() * 12,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
      }}, 0);
    }});
    
    // ===== GLOW ORBS =====
    const orbs = [];
    for (let i = 0; i < 3; i++) {{
      const orb = document.createElement('div');
      orb.className = 'glow-orb';
      orb.style.width = (200 + Math.random() * 300) + 'px';
      orb.style.height = orb.style.width;
      orb.style.background = i === 0 ? 'rgba(0,255,136,0.08)' : 
                             i === 1 ? 'rgba(255,51,102,0.06)' : 'rgba(255,215,0,0.05)';
      orb.style.left = (100 + Math.random() * 600) + 'px';
      orb.style.top = (100 + Math.random() * 800) + 'px';
      document.body.appendChild(orb);
      orbs.push(orb);
    }}
    
    // Orb float animation
    orbs.forEach((orb, i) => {{
      tl.to(orb, {{
        x: () => (Math.random() - 0.5) * 300,
        y: () => (Math.random() - 0.5) * 400,
        scale: () => 0.8 + Math.random() * 0.4,
        opacity: () => 0.3 + Math.random() * 0.5,
        duration: 15 + i * 5,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
      }}, 0);
    }});
    
    // ===== SCENE MANAGEMENT =====
    const scenes = {json.dumps([s["scene"] for s in script])};
    const sceneTimings = {json.dumps([{"id": s["scene"], "start": s["start"], "end": s["end"]} for s in script])};
    
    // Show/hide scenes
    sceneTimings.forEach(s => {{
      const el = document.getElementById('scene-' + s.id);
      if (!el) return;
      // Entrance: fade + scale + slide
      tl.to(el, {{
        opacity: 1,
        scale: 1,
        y: 0,
        duration: 0.6,
        ease: 'power3.out',
      }}, s.start);
      
      // Scene content stagger animation
      const children = el.querySelectorAll('.hero, .hero-gold, .hero-warn, .headline');
      tl.from(children, {{
        y: 40,
        opacity: 0,
        duration: 0.7,
        stagger: 0.15,
        ease: 'power2.out',
      }}, s.start + 0.2);
      
      const subs = el.querySelectorAll('.subtitle');
      tl.from(subs, {{
        y: 20,
        opacity: 0,
        duration: 0.5,
        ease: 'power2.out',
      }}, s.start + 0.6);
      
      const cards = el.querySelectorAll('.card');
      tl.from(cards, {{
        scale: 0.7,
        opacity: 0,
        duration: 0.5,
        stagger: 0.12,
        ease: 'back.out(1.7)',
      }}, s.start + 0.8);
      
      // Exit: fade out
      tl.to(el, {{
        opacity: 0,
        scale: 0.95,
        duration: 0.4,
        ease: 'power2.in',
      }}, s.end - 0.4);
    }});
    
    // Initial scene state
    gsap.set('.scene', {{ opacity: 0, scale: 0.95, y: 30 }});
    
    // ===== CAPTIONS (karaoke) =====
    const captionsEl = document.getElementById('captions');
    const captionsData = {json.dumps(script, ensure_ascii=False)};
    
    captionsData.forEach(seg => {{
      const words = seg.text.split('');
      const durPerChar = (seg.end - seg.start) / words.length;
      
      words.forEach((char, i) => {{
        const span = document.createElement('span');
        span.className = 'caption-word';
        span.textContent = char;
        span.setAttribute('data-scene', seg.scene);
        span.setAttribute('data-idx', i);
        captionsEl.appendChild(span);
        
        // Activate at the right time
        tl.set(span, {{ opacity: 0.3, color: '#FFFFFF' }}, seg.start + i * durPerChar);
        tl.to(span, {{
          opacity: 1,
          color: '#00FF88',
          scale: 1.15,
          duration: 0.15,
          ease: 'power2.out',
        }}, seg.start + i * durPerChar);
        tl.to(span, {{
          scale: 1,
          duration: 0.1,
          ease: 'power2.in',
        }}, seg.start + i * durPerChar + 0.15);
        
        // Deactivate after delay
        tl.to(span, {{
          opacity: 0.3,
          color: '#FFFFFF',
          duration: 0.3,
        }}, seg.start + i * durPerChar + durPerChar * 3);
      }});
    }});
    
    // Show captions container
    tl.set('#captions', {{ opacity: 1 }}, 0);
    
    // ===== BG GLOW PULSE =====
    tl.to('.bg-glow', {{
      opacity: 0.5,
      duration: 2,
      repeat: -1,
      yoyo: true,
      ease: 'sine.inOut',
    }}, 0);
    
    // ===== AUDIO =====
    const audio = document.getElementById('narration');
    tl.call(() => audio.play(), [], 0);
    
    // ===== REGISTER TIMELINE =====
    window.__timelines = window.__timelines || {{}};
    window.__timelines['main'] = tl;
  </script>
</body>
</html>
'''

with open('/workspace/demo_video/chuhai-fenxian/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated index.html ({len(html)} bytes)")
print(f"Total scenes: {len(script)}")
print(f"Total duration: {total_duration}s")
