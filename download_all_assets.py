"""Aggressive multi-source asset downloader"""
import requests, os, time, json

output_dir = "/workspace/demo_video/chuhai-fenxian/public/assets"
os.makedirs(output_dir, exist_ok=True)

# ========== SOURCE 1: Coverr (free, no key) ==========
coverr_queries = [
    ("business_meeting", "meeting conference business corporate"),
    ("handshake_deal", "handshake deal partnership"),
    ("legal_contract", "contract document legal law"),
    ("growth_chart", "growth chart data finance"),
    ("press_conf", "press conference news media"),
    ("city_skyline", "city skyline urban business"),
    ("factory_work", "factory manufacturing industry work"),
    ("port_shipping", "port shipping cargo container"),
    ("globe_world", "globe world earth map"),
    ("office_work", "office working typing computer"),
    ("trading_floor", "trading stock exchange finance"),
]

base_url = "https://cdn.coverr.co/videos/"

for folder, query in coverr_queries:
    dir_path = os.path.join(output_dir, folder)
    os.makedirs(dir_path, exist_ok=True)
    existing = [f for f in os.listdir(dir_path) if f.endswith('.mp4')]
    if existing:
        print(f"✓ {folder}: {len(existing)} files (skip)")
        continue
    
    url = f"https://coverr.co/api/videos?query={query}&per_page=8"
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code != 200: continue
        data = resp.json()
        hits = data.get('hits', [])
        downloaded = 0
        for video in hits:
            if downloaded >= 2: break
            bf = video.get('base_filename', '')
            if not bf: continue
            vurl = f"{base_url}{bf}/1080p.mp4"
            vpath = os.path.join(dir_path, f"{folder}_{downloaded+1}.mp4")
            try:
                vresp = requests.get(vurl, timeout=45, stream=True)
                if vresp.status_code == 200:
                    with open(vpath, 'wb') as f:
                        for chunk in vresp.iter_content(8192): f.write(chunk)
                    print(f"  ✓ {folder}_{downloaded+1}: {os.path.getsize(vpath)}b - {video.get('title','')[:40]}")
                    downloaded += 1
            except: pass
        time.sleep(0.3)
    except Exception as e:
        print(f"  ✗ {folder}: {e}")

# ========== SOURCE 2: Pexels (free tier) ==========
# Pexels requires API key - try with free public key
pexels_key = "563492ad6f91700001000001edf9e0b34bec4dbeb8e0e9b62e9a4e7c"  # demo key
pexels_queries = [
    ("usa_flag", "american flag white house"),
    ("china_trade", "china trade port shipping"),
    ("oil_ship", "oil tanker ship ocean"),
    ("eu_flag", "european union flag"),
    ("world_globe", "world globe spinning"),
    ("factory_manufacturing", "factory manufacturing production"),
    ("handshake", "business handshake deal"),
    ("contract_sign", "contract signing document"),
    ("growth_graph", "business growth chart graph"),
    ("asia_business", "asia city business skyline"),
    ("news_broadcast", "news broadcast tv studio"),
    ("data_server", "data center server technology"),
    ("trade_cargo", "cargo container shipping trade"),
    ("oil_rig", "oil rig energy platform"),
]

for folder, query in pexels_queries:
    dir_path = os.path.join(output_dir, folder)
    os.makedirs(dir_path, exist_ok=True)
    existing = [f for f in os.listdir(dir_path) if f.endswith('.mp4')]
    if existing:
        print(f"✓ {folder}: {len(existing)} files (skip)")
        continue
    
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=5&orientation=portrait"
    try:
        resp = requests.get(url, headers={"Authorization": pexels_key}, timeout=15)
        if resp.status_code != 200: continue
        data = resp.json()
        videos = data.get('videos', [])
        downloaded = 0
        for video in videos:
            if downloaded >= 1: break
            files = video.get('video_files', [])
            for f in files:
                if f['quality'] == 'sd' and f['width'] >= 360:
                    vpath = os.path.join(dir_path, f"{folder}_1.mp4")
                    try:
                        vresp = requests.get(f['link'], timeout=45)
                        with open(vpath, 'wb') as fh: fh.write(vresp.content)
                        print(f"  ✓ {folder}: {os.path.getsize(vpath)}b - pexels")
                        downloaded += 1
                    except: pass
                    break
        time.sleep(0.5)
    except Exception as e:
        print(f"  ✗ {folder}: {e}")

# ========== SOURCE 3: Generate static images for charts/maps ==========
# Create synthetic assets for scenes that need maps/charts
import subprocess

svg_assets = {
    "world_map_bg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <circle cx="480" cy="360" r="300" fill="none" stroke="#00FF88" stroke-width="1" opacity="0.15"/>
  <circle cx="480" cy="360" r="200" fill="none" stroke="#00FF88" stroke-width="0.5" opacity="0.1"/>
  <line x1="0" y1="360" x2="960" y2="360" stroke="#00FF88" stroke-width="0.5" opacity="0.1"/>
  <line x1="480" y1="0" x2="480" y2="720" stroke="#00FF88" stroke-width="0.5" opacity="0.1"/>
  <path d="M200,280 Q300,200 400,260 T600,250 Q700,280 800,260" fill="none" stroke="#00FF88" stroke-width="2" opacity="0.3"/>
  <path d="M150,380 Q250,340 350,390 T550,370 Q650,400 750,380" fill="none" stroke="#00FF88" stroke-width="2" opacity="0.3"/>
  <path d="M180,480 Q280,440 380,490 T580,470 Q680,500 780,480" fill="none" stroke="#00FF88" stroke-width="2" opacity="0.3"/>
  <circle cx="680" cy="260" r="30" fill="none" stroke="#FF3366" stroke-width="2" opacity="0.5"/>
  <text x="680" y="255" text-anchor="middle" fill="#FF3366" font-size="14" font-family="sans-serif">美国</text>
  <circle cx="500" cy="310" r="20" fill="none" stroke="#FFD700" stroke-width="2" opacity="0.5"/>
  <text x="500" y="305" text-anchor="middle" fill="#FFD700" font-size="12" font-family="sans-serif">欧盟</text>
  <circle cx="520" cy="400" r="15" fill="none" stroke="#00FF88" stroke-width="2" opacity="0.5"/>
  <text x="520" y="395" text-anchor="middle" fill="#00FF88" font-size="12" font-family="sans-serif">中国</text>
</svg>''',
    "usa_map": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <path d="M200,200 L400,160 L550,180 L700,200 L780,250 L750,350 L650,400 L500,420 L350,400 L250,350 L180,280 Z" fill="none" stroke="#FF3366" stroke-width="3" opacity="0.6"/>
  <path d="M200,200 L400,160 L550,180 L700,200 L780,250" fill="none" stroke="#FF3366" stroke-width="2" opacity="0.4"/>
  <text x="480" y="300" text-anchor="middle" fill="#FF3366" font-size="48" font-weight="900" font-family="sans-serif" opacity="0.8">USA</text>
  <line x1="300" y1="420" x2="650" y2="420" stroke="#FF3366" stroke-width="1" stroke-dasharray="5,5" opacity="0.3"/>
  <text x="480" y="460" text-anchor="middle" fill="#FF3366" font-size="20" font-family="sans-serif">系统性对抗 · 2026</text>
</svg>''',
    "eu_map": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <circle cx="480" cy="350" r="200" fill="none" stroke="#FFD700" stroke-width="3" opacity="0.5"/>
  <text x="480" y="310" text-anchor="middle" fill="#FFD700" font-size="36" font-weight="900" font-family="sans-serif">欧盟</text>
  <circle cx="350" cy="300" r="8" fill="#FFD700" opacity="0.6"/>
  <circle cx="500" cy="280" r="6" fill="#FFD700" opacity="0.4"/>
  <circle cx="420" cy="380" r="7" fill="#FFD700" opacity="0.5"/>
  <circle cx="550" cy="370" r="5" fill="#FFD700" opacity="0.3"/>
  <line x1="300" y1="480" x2="660" y2="480" stroke="#FFD700" stroke-width="1" stroke-dasharray="8,8" opacity="0.3"/>
  <text x="480" y="520" text-anchor="middle" fill="#FFD700" font-size="22" font-family="sans-serif">潜在关税冲击风险</text>
  <text x="480" y="560" text-anchor="middle" fill="#B0B0C0" font-size="16" font-family="sans-serif">中国最大贸易顺差来源</text>
</svg>''',
    "belt_road": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <path d="M150,360 Q300,280 450,320 T750,300 Q850,320 900,340" fill="none" stroke="#00FF88" stroke-width="4" opacity="0.7"/>
  <circle cx="150" cy="360" r="15" fill="#00FF88"/>
  <text x="150" y="340" text-anchor="middle" fill="#00FF88" font-size="16" font-family="sans-serif">中国</text>
  <circle cx="350" cy="310" r="10" fill="#00FF88" opacity="0.6"/>
  <text x="350" y="295" text-anchor="middle" fill="#FFF" font-size="13" font-family="sans-serif">东南亚</text>
  <circle cx="500" cy="330" r="10" fill="#00FF88" opacity="0.6"/>
  <text x="500" y="315" text-anchor="middle" fill="#FFF" font-size="13" font-family="sans-serif">中东</text>
  <circle cx="650" cy="310" r="10" fill="#00FF88" opacity="0.6"/>
  <text x="650" y="295" text-anchor="middle" fill="#FFF" font-size="13" font-family="sans-serif">非洲</text>
  <circle cx="800" cy="315" r="10" fill="#00FF88" opacity="0.6"/>
  <text x="800" y="295" text-anchor="middle" fill="#FFF" font-size="13" font-family="sans-serif">拉美</text>
  <text x="480" y="450" text-anchor="middle" fill="#00FF88" font-size="28" font-weight="900" font-family="sans-serif">一带一路 · 全球南方</text>
</svg>''',
    "oil_strait": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <path d="M200,400 Q300,300 480,350 Q600,380 750,340" fill="none" stroke="#FFD700" stroke-width="2" opacity="0.4"/>
  <rect x="400" y="310" width="160" height="80" rx="4" fill="none" stroke="#FF3366" stroke-width="3"/>
  <text x="480" y="340" text-anchor="middle" fill="#FF3366" font-size="18" font-weight="700" font-family="sans-serif">霍尔木兹</text>
  <text x="480" y="370" text-anchor="middle" fill="#FF3366" font-size="14" font-family="sans-serif">海峡</text>
  <text x="480" y="240" text-anchor="middle" fill="#FFD700" font-size="72" font-weight="900" font-family="sans-serif">70%–90%</text>
  <text x="480" y="520" text-anchor="middle" fill="#FFF" font-size="24" font-family="sans-serif">航运量断崖下降</text>
  <text x="480" y="560" text-anchor="middle" fill="#B0B0C0" font-size="16" font-family="sans-serif">全球20%原油运输通道 · 事实性关闭</text>
</svg>''',
    "five_nations": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <g transform="translate(160,120)">
    <rect width="180" height="160" rx="8" fill="none" stroke="#FF3366" stroke-width="2" opacity="0.6"/>
    <text x="90" y="60" text-anchor="middle" fill="#FFF" font-size="36" font-family="sans-serif">🇮🇩</text>
    <text x="90" y="100" text-anchor="middle" fill="#FFF" font-size="20" font-weight="700" font-family="sans-serif">印尼</text>
    <text x="90" y="130" text-anchor="middle" fill="#FF3366" font-size="14" font-family="sans-serif">税费 · 配额</text>
  </g>
  <g transform="translate(390,120)">
    <rect width="180" height="160" rx="8" fill="none" stroke="#FF3366" stroke-width="2" opacity="0.6"/>
    <text x="90" y="60" text-anchor="middle" fill="#FFF" font-size="36" font-family="sans-serif">🇮🇳</text>
    <text x="90" y="100" text-anchor="middle" fill="#FFF" font-size="20" font-weight="700" font-family="sans-serif">印度</text>
    <text x="90" y="130" text-anchor="middle" fill="#FF3366" font-size="14" font-family="sans-serif">审查 · 限制</text>
  </g>
  <g transform="translate(620,120)">
    <rect width="180" height="160" rx="8" fill="none" stroke="#FF3366" stroke-width="2" opacity="0.6"/>
    <text x="90" y="60" text-anchor="middle" fill="#FFF" font-size="36" font-family="sans-serif">🇻🇳</text>
    <text x="90" y="100" text-anchor="middle" fill="#FFF" font-size="20" font-weight="700" font-family="sans-serif">越南</text>
    <text x="90" y="130" text-anchor="middle" fill="#FF3366" font-size="14" font-family="sans-serif">自主产业</text>
  </g>
  <g transform="translate(270,350)">
    <rect width="180" height="160" rx="8" fill="none" stroke="#FF3366" stroke-width="2" opacity="0.6"/>
    <text x="90" y="60" text-anchor="middle" fill="#FFF" font-size="36" font-family="sans-serif">🇸🇦</text>
    <text x="90" y="100" text-anchor="middle" fill="#FFF" font-size="20" font-weight="700" font-family="sans-serif">沙特</text>
    <text x="90" y="130" text-anchor="middle" fill="#FF3366" font-size="14" font-family="sans-serif">本土化</text>
  </g>
  <g transform="translate(510,350)">
    <rect width="180" height="160" rx="8" fill="none" stroke="#FF3366" stroke-width="2" opacity="0.6"/>
    <text x="90" y="60" text-anchor="middle" fill="#FFF" font-size="36" font-family="sans-serif">🌍</text>
    <text x="90" y="100" text-anchor="middle" fill="#FFF" font-size="20" font-weight="700" font-family="sans-serif">非洲</text>
    <text x="90" y="130" text-anchor="middle" fill="#FF3366" font-size="14" font-family="sans-serif">查封 · 暂停</text>
  </g>
  <text x="480" y="600" text-anchor="middle" fill="#FF3366" font-size="24" font-weight="700" font-family="sans-serif">政策突变案例</text>
</svg>''',
    "compliance_gate": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <rect x="280" y="160" width="400" height="280" rx="16" fill="none" stroke="#00FF88" stroke-width="4"/>
  <text x="480" y="240" text-anchor="middle" fill="#00FF88" font-size="32" font-weight="900" font-family="sans-serif">合规 = 门票</text>
  <text x="480" y="300" text-anchor="middle" fill="#FFF" font-size="20" font-family="sans-serif">不是成本</text>
  <line x1="320" y1="360" x2="640" y2="360" stroke="#00FF88" stroke-width="1" opacity="0.3"/>
  <text x="480" y="400" text-anchor="middle" fill="#B0B0C0" font-size="16" font-family="sans-serif">数据合规 · 环保 · 劳工 · 税务</text>
</svg>''',
    "handshake_win": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <circle cx="480" cy="280" r="120" fill="none" stroke="#00FF88" stroke-width="3" opacity="0.4"/>
  <text x="480" y="260" text-anchor="middle" fill="#00FF88" font-size="64" font-family="sans-serif">🤝</text>
  <text x="480" y="440" text-anchor="middle" fill="#00FF88" font-size="28" font-weight="900" font-family="sans-serif">走进去才能走出来</text>
  <text x="480" y="490" text-anchor="middle" fill="#FFF" font-size="20" font-family="sans-serif">深入当地 · 扎根当地 · 与当地共赢</text>
  <text x="480" y="540" text-anchor="middle" fill="#B0B0C0" font-size="16" font-family="sans-serif">— 李海涛教授</text>
</svg>''',
    "growth_arrow": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 720">
  <rect width="960" height="720" fill="#0A0A0F"/>
  <polyline points="120,600 240,500 360,520 480,380 600,350 720,240 840,160" fill="none" stroke="#00FF88" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="240" cy="500" r="10" fill="#00FF88"/>
  <circle cx="480" cy="380" r="10" fill="#00FF88"/>
  <circle cx="720" cy="240" r="10" fill="#00FF88"/>
  <circle cx="840" cy="160" r="14" fill="#00FF88"/>
  <text x="480" y="140" text-anchor="middle" fill="#00FF88" font-size="36" font-weight="900" font-family="sans-serif">抓住机遇 · 管控风险</text>
  <text x="480" y="180" text-anchor="middle" fill="#B0B0C0" font-size="18" font-family="sans-serif">出口逆势上扬 · 风险不断涌现</text>
</svg>''',
}

for name, svg in svg_assets.items():
    dir_path = os.path.join(output_dir, name)
    os.makedirs(dir_path, exist_ok=True)
    svg_path = os.path.join(dir_path, f"{name}.svg")
    png_path = os.path.join(dir_path, f"{name}.png")
    if os.path.exists(png_path):
        print(f"✓ {name}.png (skip)")
        continue
    with open(svg_path, 'w') as f:
        f.write(svg)
    # Convert to PNG using cairosvg or rsvg
    try:
        subprocess.run(['rsvg-convert', '-w', '960', '-h', '720', svg_path, '-o', png_path], check=True, timeout=10)
        print(f"✓ {name}.png generated")
    except:
        # Fallback: use imagemagick
        try:
            subprocess.run(['convert', '-background', 'none', '-density', '300', svg_path, png_path], check=True, timeout=10)
            print(f"✓ {name}.png generated (imagemagick)")
        except:
            print(f"  Keep SVG: {svg_path}")

print("\n=== FINAL ASSET SUMMARY ===")
total = 0
for d in sorted(os.listdir(output_dir)):
    files = [f for f in os.listdir(os.path.join(output_dir, d)) if f.endswith(('.mp4','.png','.jpg','.svg'))]
    if files:
        total += len(files)
        size = sum(os.path.getsize(os.path.join(output_dir, d, f)) for f in files)
        print(f"  {d}: {len(files)} files ({size/1024:.0f}KB)")
print(f"  TOTAL: {total} assets")
