import os

# Frame templates based on STORYBOARD_ENRICHED
frames = [
    {
        "id": "01-hook-shock",
        "duration": 5,
        "title": "政策一夜变卦",
        "subtitle": "出海最大的敌人不是竞争对手",
        "type": "hook",
        "accent": "#00FF88",
        "warn": False,
        "elements": [
            {"type": "text", "content": "政策一夜变卦", "style": "hero", "y": 300},
            {"type": "text", "content": "出海最大的敌人不是竞争对手", "style": "subtitle", "y": 420},
            {"type": "icon", "content": "warning", "y": 160, "x": 900},
            {"type": "map", "style": "world-outline", "y": 550}
        ]
    },
    {
        "id": "02-speaker-intro",
        "duration": 4,
        "title": "李海涛教授",
        "subtitle": "长江商学院院长",
        "type": "intro",
        "accent": "#FFD700",
        "warn": False,
        "elements": [
            {"type": "text", "content": "李海涛教授", "style": "hero-gold", "y": 300},
            {"type": "text", "content": "长江商学院院长", "style": "subtitle", "y": 420},
            {"type": "text", "content": "第十二届中国企业走出去风险发布会", "style": "label", "y": 520}
        ]
    },
    {
        "id": "03-risk-overview",
        "duration": 6,
        "title": "三大风险",
        "subtitle": "",
        "type": "list",
        "accent": "#00FF88",
        "warn": False,
        "elements": [
            {"type": "text", "content": "三大风险", "style": "headline", "y": 150},
            {"type": "card", "content": "01\n美国系统性对抗", "y": 320, "x": 80},
            {"type": "card", "content": "02\n当地政府政策突变", "y": 320, "x": 400},
            {"type": "card", "content": "03\n欧盟潜在风险", "y": 320, "x": 720}
        ]
    },
    {
        "id": "04-risk-usa",
        "duration": 7,
        "title": "美国系统性对抗",
        "subtitle": "2026年特朗普政府系列操作",
        "type": "data",
        "accent": "#FF3366",
        "warn": True,
        "elements": [
            {"type": "text", "content": "美国系统性对抗", "style": "hero", "y": 250},
            {"type": "text", "content": "2026", "style": "data-accent", "y": 350},
            {"type": "map", "style": "usa-outline", "y": 450},
            {"type": "icon", "content": "tariff", "y": 200, "x": 850}
        ]
    },
    {
        "id": "05-risk-usa-detail",
        "duration": 6,
        "title": "一带一路",
        "subtitle": "全球南方布局",
        "type": "map",
        "accent": "#00FF88",
        "warn": False,
        "elements": [
            {"type": "text", "content": "全球南方", "style": "headline-accent", "y": 150},
            {"type": "map", "style": "world-south", "y": 300},
            {"type": "label", "content": "委内瑞拉 · 古巴 · 霍尔木兹", "style": "tags", "y": 1050}
        ]
    },
    {
        "id": "06-risk-usa-impact",
        "duration": 8,
        "title": "70%-90%",
        "subtitle": "霍尔木兹海峡航运量下降",
        "type": "data-shock",
        "accent": "#FFD700",
        "warn": True,
        "elements": [
            {"type": "text", "content": "70%-90%", "style": "data-gold", "y": 280},
            {"type": "text", "content": "航运量大幅下降", "style": "subtitle", "y": 450},
            {"type": "map", "style": "strait", "y": 550},
            {"type": "icon", "content": "arrow-down", "y": 300, "x": 750}
        ]
    },
    {
        "id": "07-risk-policy",
        "duration": 5,
        "title": "政策突变",
        "subtitle": "当地政府政策一夜之间变卦",
        "type": "shock",
        "accent": "#FF3366",
        "warn": True,
        "elements": [
            {"type": "text", "content": "政策突变", "style": "hero-warn", "y": 350},
            {"type": "text", "content": "一夜之间", "style": "subtitle-warn", "y": 480},
            {"type": "icon", "content": "warning-flash", "y": 200, "x": 900}
        ]
    },
    {
        "id": "08-risk-policy-examples",
        "duration": 9,
        "title": "政策突变案例",
        "subtitle": "",
        "type": "card-grid",
        "accent": "#FF3366",
        "warn": True,
        "elements": [
            {"type": "text", "content": "政策突变案例", "style": "headline", "y": 120},
            {"type": "card-small", "content": "印尼\n税费增加·镍矿配额削减", "y": 280, "x": 80},
            {"type": "card-small", "content": "印度\n严格审查·限制升级", "y": 280, "x": 400},
            {"type": "card-small", "content": "越南\n自主产业·降低依赖", "y": 280, "x": 720},
            {"type": "card-small", "content": "沙特\n本土化比例提升", "y": 620, "x": 80},
            {"type": "card-small", "content": "非洲\n查封账户·暂停出口", "y": 620, "x": 400}
        ]
    },
    {
        "id": "09-risk-eu",
        "duration": 7,
        "title": "欧盟潜在风险",
        "subtitle": "最大贸易顺差来源面临冲击",
        "type": "data",
        "accent": "#FFD700",
        "warn": False,
        "elements": [
            {"type": "text", "content": "欧盟潜在风险", "style": "hero", "y": 250},
            {"type": "arrow", "content": "中国 → 欧盟", "style": "trade-flow", "y": 400},
            {"type": "map", "style": "eu-outline", "y": 600},
            {"type": "icon", "content": "euro", "y": 200, "x": 850}
        ]
    },
    {
        "id": "10-solution-overview",
        "duration": 4,
        "title": "三大应对之道",
        "subtitle": "",
        "type": "list",
        "accent": "#00FF88",
        "warn": False,
        "elements": [
            {"type": "text", "content": "三大应对之道", "style": "headline", "y": 150},
            {"type": "card", "content": "01\n地缘洞察能力", "y": 320, "x": 80},
            {"type": "card", "content": "02\n合规能力", "y": 320, "x": 400},
            {"type": "card", "content": "03\n本地化执行能力", "y": 320, "x": 720}
        ]
    },
    {
        "id": "11-solution-1",
        "duration": 7,
        "title": "地缘洞察能力",
        "subtitle": "不能只算经济账，不算政治账",
        "type": "concept",
        "accent": "#FFD700",
        "warn": False,
        "elements": [
            {"type": "text", "content": "地缘洞察能力", "style": "hero-gold", "y": 250},
            {"type": "radar", "style": "insight", "y": 400},
            {"type": "map", "style": "world-risk", "y": 750},
            {"type": "text", "content": "老板的认知边界，就是企业出海的天花板", "style": "quote", "y": 1150}
        ]
    },
    {
        "id": "12-solution-2",
        "duration": 6,
        "title": "合规能力",
        "subtitle": "合规是门票，不是成本",
        "type": "concept",
        "accent": "#00FF88",
        "warn": False,
        "elements": [
            {"type": "text", "content": "合规能力", "style": "hero", "y": 250},
            {"type": "icon", "content": "ticket", "y": 400, "x": 450},
            {"type": "text", "content": "数据合规 · 环保 · 劳工 · 税务", "style": "tags", "y": 700},
            {"type": "text", "content": "合规是门票，不是成本", "style": "quote-accent", "y": 900}
        ]
    },
    {
        "id": "13-solution-3",
        "duration": 7,
        "title": "本地化执行能力",
        "subtitle": '走进去才能走出来',
        "type": "concept",
        "accent": "#00FF88",
        "warn": False,
        "elements": [
            {"type": "text", "content": "本地化执行能力", "style": "hero", "y": 250},
            {"type": "icon", "content": "handshake", "y": 400, "x": 420},
            {"type": "text", "content": '走进去才能走出来', "style": "quote-accent", "y": 750}
        ]
    },
    {
        "id": "14-closing-quote",
        "duration": 8,
        "title": '走进去才能走出来',
        "subtitle": "李海涛教授",
        "type": "quote",
        "accent": "#FFD700",
        "warn": False,
        "elements": [
            {"type": "text", "content": "'走进去才能走出来'", "style": "hero-gold", "y": 350},
            {"type": "text", "content": "深入当地 · 扎根当地 · 与当地共赢", "style": "subtitle", "y": 550},
            {"type": "text", "content": "— 李海涛教授", "style": "label", "y": 700}
        ]
    },
    {
        "id": "15-cta-summary",
        "duration": 6,
        "title": "抓住机遇 · 管控风险",
        "subtitle": "出口逆势上扬，风险不断涌现",
        "type": "cta",
        "accent": "#00FF88",
        "warn": False,
        "elements": [
            {"type": "text", "content": "抓住机遇 · 管控风险", "style": "hero", "y": 300},
            {"type": "icon", "content": "arrow-up", "y": 450, "x": 480},
            {"type": "chart", "style": "growth", "y": 650}
        ]
    }
]

# HTML template
def generate_frame_html(frame):
    bg_color = "#0A0A0F"
    accent = frame["accent"]
    warn_color = "#FF3366"
    
    elements_html = ""
    for el in frame["elements"]:
        if el["type"] == "text":
            style = el.get("style", "body")
            color = "#FFFFFF"
            font_size = "32px"
            font_weight = "500"
            
            if style == "hero":
                font_size = "72px"
                font_weight = "900"
            elif style == "hero-gold":
                font_size = "72px"
                font_weight = "900"
                color = "#FFD700"
            elif style == "hero-warn":
                font_size = "80px"
                font_weight = "900"
                color = warn_color
            elif style == "headline":
                font_size = "48px"
                font_weight = "700"
            elif style == "headline-accent":
                font_size = "48px"
                font_weight = "700"
                color = accent
            elif style == "subtitle":
                font_size = "40px"
                font_weight = "500"
                color = "#B0B0C0"
            elif style == "subtitle-warn":
                font_size = "40px"
                font_weight = "700"
                color = warn_color
            elif style == "data-gold":
                font_size = "120px"
                font_weight = "700"
                color = "#FFD700"
            elif style == "data-accent":
                font_size = "48px"
                font_weight = "700"
                color = accent
            elif style == "label":
                font_size = "24px"
                font_weight = "400"
                color = "#666666"
            elif style == "quote":
                font_size = "28px"
                font_weight = "500"
                color = "#B0B0C0"
            elif style == "quote-accent":
                font_size = "36px"
                font_weight = "600"
                color = accent
            elif style == "tags":
                font_size = "28px"
                font_weight = "500"
                color = "#B0B0C0"
            
            elements_html += f'''
      <div class="el-text" style="top:{el['y']}px; color:{color}; font-size:{font_size}; font-weight:{font_weight};">
        {el['content'].replace(chr(10), '<br>')}
      </div>'''
            
        elif el["type"] == "card":
            x = el.get("x", 80)
            elements_html += f'''
      <div class="el-card" style="top:{el['y']}px; left:{x}px;">
        {el['content'].replace(chr(10), '<br>')}
      </div>'''
            
        elif el["type"] == "card-small":
            x = el.get("x", 80)
            elements_html += f'''
      <div class="el-card-small" style="top:{el['y']}px; left:{x}px;">
        {el['content'].replace(chr(10), '<br>')}
      </div>'''
            
        elif el["type"] == "icon":
            x = el.get("x", 900)
            icon_svg = ""
            if el["content"] == "warning":
                icon_svg = '<svg viewBox="0 0 80 80"><polygon points="40,10 70,70 10,70" fill="none" stroke="#FF3366" stroke-width="3"/><line x1="40" y1="30" x2="40" y2="50" stroke="#FF3366" stroke-width="3" stroke-linecap="round"/><circle cx="40" cy="58" r="3" fill="#FF3366"/></svg>'
            elif el["content"] == "arrow-down":
                icon_svg = '<svg viewBox="0 0 80 80"><line x1="40" y1="10" x2="40" y2="60" stroke="#FF3366" stroke-width="6" stroke-linecap="round"/><polyline points="20,45 40,65 60,45" fill="none" stroke="#FF3366" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            elif el["content"] == "arrow-up":
                icon_svg = '<svg viewBox="0 0 80 80"><line x1="40" y1="70" x2="40" y2="20" stroke="#00FF88" stroke-width="6" stroke-linecap="round"/><polyline points="20,35 40,15 60,35" fill="none" stroke="#00FF88" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            elif el["content"] == "ticket":
                icon_svg = '<svg viewBox="0 0 100 60"><rect x="5" y="5" width="90" height="50" rx="8" fill="none" stroke="#FFD700" stroke-width="3"/><circle cx="20" cy="30" r="8" fill="#FFD700"/><text x="55" y="35" text-anchor="middle" fill="#FFD700" font-size="16" font-weight="bold">TICKET</text></svg>'
            elif el["content"] == "handshake":
                icon_svg = '<svg viewBox="0 0 100 80"><path d="M20,40 Q30,20 50,30 Q70,20 80,40" fill="none" stroke="#00FF88" stroke-width="4" stroke-linecap="round"/><circle cx="30" cy="50" r="15" fill="none" stroke="#00FF88" stroke-width="3"/><circle cx="70" cy="50" r="15" fill="none" stroke="#00FF88" stroke-width="3"/></svg>'
            elif el["content"] == "warning-flash":
                icon_svg = '<svg viewBox="0 0 80 80"><polygon points="40,10 70,70 10,70" fill="none" stroke="#FF3366" stroke-width="4"/><line x1="40" y1="30" x2="40" y2="50" stroke="#FF3366" stroke-width="4" stroke-linecap="round"/><circle cx="40" cy="58" r="4" fill="#FF3366"/></svg>'
            elif el["content"] == "tariff":
                icon_svg = '<svg viewBox="0 0 80 80"><rect x="15" y="20" width="50" height="40" rx="4" fill="none" stroke="#FF3366" stroke-width="3"/><text x="40" y="48" text-anchor="middle" fill="#FF3366" font-size="20" font-weight="bold">$</text></svg>'
            elif el["content"] == "euro":
                icon_svg = '<svg viewBox="0 0 80 80"><circle cx="40" cy="40" r="30" fill="none" stroke="#FFD700" stroke-width="3"/><text x="40" y="50" text-anchor="middle" fill="#FFD700" font-size="28" font-weight="bold">€</text></svg>'
            
            elements_html += f'''
      <div class="el-icon" style="top:{el['y']}px; left:{x}px;">
        {icon_svg}
      </div>'''
            
        elif el["type"] == "map":
            elements_html += f'''
      <div class="el-map" style="top:{el['y']}px;">
        <svg viewBox="0 0 900 400" style="width:900px;height:400px;">
          <path d="M100,200 Q200,150 350,180 T550,200 Q650,170 750,190 T850,200" fill="none" stroke="{accent}" stroke-width="1" opacity="0.3"/>
          <path d="M50,280 Q150,260 250,300 T450,280 Q550,300 650,270 T800,280" fill="none" stroke="{accent}" stroke-width="1" opacity="0.3"/>
          <line x1="0" y1="200" x2="900" y2="200" stroke="{accent}" stroke-dasharray="5,5" opacity="0.2"/>
          <line x1="450" y1="0" x2="450" y2="400" stroke="{accent}" stroke-dasharray="5,5" opacity="0.2"/>
        </svg>
      </div>'''
            
        elif el["type"] == "radar":
            elements_html += f'''
      <div class="el-radar" style="top:{el['y']}px;">
        <svg viewBox="0 0 300 300" style="width:300px;height:300px;">
          <circle cx="150" cy="150" r="120" fill="none" stroke="#FFD700" stroke-width="1" opacity="0.3"/>
          <circle cx="150" cy="150" r="80" fill="none" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <circle cx="150" cy="150" r="40" fill="none" stroke="#FFD700" stroke-width="1" opacity="0.1"/>
          <line x1="150" y1="30" x2="150" y2="270" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <line x1="30" y1="150" x2="270" y2="150" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <line x1="65" y1="65" x2="235" y2="235" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
          <line x1="65" y1="235" x2="235" y2="65" stroke="#FFD700" stroke-width="1" opacity="0.2"/>
        </svg>
      </div>'''
            
        elif el["type"] == "chart":
            elements_html += f'''
      <div class="el-chart" style="top:{el['y']}px;">
        <svg viewBox="0 0 800 300" style="width:800px;height:300px;">
          <polyline points="50,250 150,200 250,180 350,150 450,120 550,100 650,80 750,50" fill="none" stroke="#00FF88" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="150" cy="200" r="6" fill="#00FF88"/>
          <circle cx="250" cy="180" r="6" fill="#00FF88"/>
          <circle cx="350" cy="150" r="6" fill="#00FF88"/>
          <circle cx="450" cy="120" r="6" fill="#00FF88"/>
          <circle cx="550" cy="100" r="6" fill="#00FF88"/>
          <circle cx="650" cy="80" r="6" fill="#00FF88"/>
          <circle cx="750" cy="50" r="6" fill="#00FF88"/>
        </svg>
      </div>'''
            
        elif el["type"] == "arrow":
            elements_html += f'''
      <div class="el-arrow" style="top:{el['y']}px;">
        <svg viewBox="0 0 400 80" style="width:400px;height:80px;">
          <line x1="50" y1="40" x2="320" y2="40" stroke="#00FF88" stroke-width="4" stroke-linecap="round"/>
          <polyline points="300,25 340,40 300,55" fill="none" stroke="#00FF88" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="30" y="30" text-anchor="middle" fill="#FFFFFF" font-size="16">中国</text>
          <text x="370" y="30" text-anchor="middle" fill="#FFFFFF" font-size="16">欧盟</text>
        </svg>
      </div>'''
    
    # Generate animation timeline
    anim_script = f"""
      const tl = gsap.timeline({{ paused: true }});
      
      // Scene 1: Background elements
      tl.from('.grid-bg', {{ opacity: 0, duration: 0.8 }}, 0);
      tl.from('.gradient-overlay', {{ opacity: 0, duration: 1.0 }}, 0);
      
      // Scene 2: Title reveal
      tl.from('.el-text', {{ 
        y: 40, 
        opacity: 0, 
        duration: 1.0, 
        stagger: 0.2,
        ease: 'power2.out' 
      }}, 0.5);
      
      // Scene 3: Cards/Icons
      tl.from('.el-card, .el-card-small', {{ 
        scale: 0.8, 
        opacity: 0, 
        duration: 0.6, 
        stagger: 0.15,
        ease: 'back.out(1.7)' 
      }}, 1.0);
      
      tl.from('.el-icon', {{ 
        scale: 0, 
        opacity: 0, 
        duration: 0.5, 
        ease: 'back.out(2)' 
     }}, 1.2);
      
      // Scene 4: Maps/Charts
      tl.from('.el-map svg path, .el-radar svg circle, .el-radar svg line', {{ 
        strokeDashoffset: 1000,
        strokeDasharray: 1000,
        duration: 2.0,
        stagger: 0.1,
        ease: 'power2.inOut'
      }}, 1.5);
      
      tl.from('.el-chart svg polyline', {{ 
        strokeDashoffset: 1000,
        strokeDasharray: 1000,
        duration: 2.0,
        ease: 'power2.inOut'
      }}, 1.5);
      
      tl.from('.el-chart svg circle', {{ 
        scale: 0, 
        opacity: 0, 
        duration: 0.3, 
        stagger: 0.1,
        ease: 'back.out(2)' 
      }}, 2.5);
      
      // Scene 5: Sustained animation
      tl.to('.el-icon', {{ 
        scale: 1.1, 
        duration: 0.5, 
        yoyo: true, 
        repeat: -1,
        ease: 'power2.inOut' 
     }}, 3.0);
      
      window.__timelines = window.__timelines || {{}};
      window.__timelines['{frame["id"]}'] = tl;
"""
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1080, height=1440">
  <title>Frame: {frame["id"]}</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    
    body {{
      width: 1080px;
      height: 1440px;
      background: {bg_color};
      font-family: 'Noto Sans SC', 'PingFang SC', sans-serif;
      overflow: hidden;
      position: relative;
    }}
    
    .grid-bg {{
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(#1A1A2E 1px, transparent 1px),
        linear-gradient(90deg, #1A1A2E 1px, transparent 1px);
      background-size: 60px 60px;
      opacity: 0.6;
    }}
    
    .gradient-overlay {{
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 40%, #1a1a2e 0%, #0a0a0f 70%);
    }}
    
    .scene-content {{
      position: relative;
      z-index: 10;
      width: 100%;
      height: 100%;
      padding: 80px;
    }}
    
    .el-text {{
      position: absolute;
      left: 80px;
      right: 80px;
      text-align: center;
      line-height: 1.2;
    }}
    
    .el-card {{
      position: absolute;
      width: 280px;
      height: 360px;
      background: rgba(0, 255, 136, 0.08);
      border: 2px solid {accent};
      border-radius: 16px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: #FFFFFF;
      font-size: 28px;
      font-weight: 600;
      line-height: 1.4;
      box-shadow: 0 0 40px rgba(0, 255, 136, 0.2);
    }}
    
    .el-card-small {{
      position: absolute;
      width: 200px;
      height: 280px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: #FFFFFF;
      font-size: 22px;
      font-weight: 500;
      line-height: 1.4;
    }}
    
    .el-icon {{
      position: absolute;
      width: 80px;
      height: 80px;
    }}
    
    .el-icon svg {{
      width: 100%;
      height: 100%;
    }}
    
    .el-map {{
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      opacity: 0.15;
    }}
    
    .el-radar {{
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      opacity: 0.3;
    }}
    
    .el-chart {{
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
    }}
    
    .el-arrow {{
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
    }}
    
    .host-zone {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 200px;
      border-top: 2px dashed rgba(0, 255, 136, 0.2);
      background: linear-gradient(to top, rgba(0,0,0,0.3), transparent);
      z-index: 5;
    }}
  </style>
</head>
<body>
  <div class="grid-bg"></div>
  <div class="gradient-overlay"></div>
  
  <div class="scene-content">
    {elements_html}
  </div>
  
  <div class="host-zone"></div>
  
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      {anim_script}
    }});
  </script>
</body>
</html>'''
    
    return html

# Generate all frames
output_dir = "/workspace/demo_video/chuhai-fenxian/compositions/frames"
os.makedirs(output_dir, exist_ok=True)

for frame in frames:
    html = generate_frame_html(frame)
    filepath = os.path.join(output_dir, f"{frame['id']}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {filepath}")

print(f"\nTotal: {len(frames)} frames generated")
