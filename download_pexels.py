"""Download free stock footage from Pexels"""
import requests
import os
import time

output_dir = "/workspace/demo_video/chuhai-fenxian/public/assets"
os.makedirs(output_dir, exist_ok=True)

# Queries matched to video content needs
queries = [
    ("usa_politics", "president politics white house"),
    ("global_trade", "global trade shipping cargo"),
    ("oil_energy", "oil energy tanker ship"),
    ("europe_flag", "european union flag brussels"),
    ("world_map", "world map global earth"),
    ("factory_industry", "factory manufacturing industry"),
    ("business_deal", "business handshake deal meeting"),
    ("legal_document", "law document contract legal"),
    ("growth_finance", "business growth finance chart"),
    ("asia_city", "asia city skyline business"),
]

for folder, query in queries:
    dir_path = os.path.join(output_dir, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    # Skip if already downloaded
    existing = [f for f in os.listdir(dir_path) if f.endswith('.mp4')]
    if existing:
        print(f"✓ {folder}: already has {len(existing)} files")
        continue
    
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=3&orientation=portrait"
    try:
        resp = requests.get(url, headers={"Authorization": "Bearer test"}, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            hits = data.get('videos', [])
            print(f"  {folder}: found {len(hits)} videos")
            
            for i, video in enumerate(hits[:2]):
                files = video.get('video_files', [])
                # Prefer sd quality
                best = None
                for f in files:
                    if f['quality'] == 'sd' and f['width'] >= 360:
                        best = f
                        break
                if not best:
                    best = files[0] if files else None
                
                if best:
                    vurl = best['link']
                    vname = f"{folder}_{i+1}.mp4"
                    vpath = os.path.join(dir_path, vname)
                    try:
                        vresp = requests.get(vurl, timeout=30)
                        with open(vpath, 'wb') as f:
                            f.write(vresp.content)
                        print(f"    ✓ {vname}: {len(vresp.content)} bytes")
                    except Exception as e:
                        print(f"    ✗ {vname}: {e}")
            time.sleep(1)
    except Exception as e:
        print(f"  ✗ {folder}: {e}")

print("\nDone!")
