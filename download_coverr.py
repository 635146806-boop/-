"""Download free stock footage from Coverr for video backgrounds"""
import requests, os, time

output_dir = "/workspace/demo_video/chuhai-fenxian/public/assets"
os.makedirs(output_dir, exist_ok=True)

# Specific searches matching our content
searches = [
    ("usa_politics", "president white house"),
    ("shipping_port", "port shipping cargo"),
    ("oil_tanker", "oil tanker ship"),
    ("europe_flag", "europe flag union"),
    ("world_globe", "world globe map earth"),
    ("factory", "factory manufacturing"),
    ("business_meeting", "business meeting handshake"),
    ("legal_docs", "legal document contract"),
    ("growth_data", "growth data chart finance"),
    ("asia_skyline", "asia city skyline"),
    ("trade_container", "shipping container cargo trade"),
    ("news_conference", "press conference news"),
]

base_url = "https://cdn.coverr.co/videos/"

for folder, query in searches:
    dir_path = os.path.join(output_dir, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    existing = [f for f in os.listdir(dir_path) if f.endswith('.mp4')]
    if existing:
        print(f"✓ {folder}: {len(existing)} files")
        continue
    
    url = f"https://coverr.co/api/videos?query={query}&per_page=5"
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code != 200:
            continue
        data = resp.json()
        hits = data.get('hits', [])
        print(f"  {folder}: {len(hits)} results")
        
        downloaded = 0
        for video in hits:
            if downloaded >= 1:
                break
            bf = video.get('base_filename', '')
            if not bf:
                continue
            
            # Coverr CDN URL pattern
            vurl = f"{base_url}{bf}/1080p.mp4"
            vname = f"{folder}_1.mp4"
            vpath = os.path.join(dir_path, vname)
            
            try:
                vresp = requests.get(vurl, timeout=30, stream=True)
                if vresp.status_code == 200:
                    with open(vpath, 'wb') as f:
                        for chunk in vresp.iter_content(8192):
                            f.write(chunk)
                    size = os.path.getsize(vpath)
                    print(f"    ✓ {vname}: {size} bytes - {video.get('title','')[:50]}")
                    downloaded += 1
                else:
                    # Try without 1080p suffix
                    vurl2 = f"{base_url}{bf}/original.mp4"
                    vresp2 = requests.get(vurl2, timeout=30, stream=True)
                    if vresp2.status_code == 200:
                        with open(vpath, 'wb') as f:
                            for chunk in vresp2.iter_content(8192):
                                f.write(chunk)
                        size = os.path.getsize(vpath)
                        print(f"    ✓ {vname}: {size} bytes")
                        downloaded += 1
            except Exception as e:
                print(f"    ✗ {e}")
        time.sleep(0.5)
    except Exception as e:
        print(f"  ✗ {folder}: {e}")

print("\nDone!")
