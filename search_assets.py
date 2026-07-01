"""Search and download relevant stock footage for the video"""
import requests
import os
import json

output_dir = "/workspace/demo_video/chuhai-fenxian/public/assets"
os.makedirs(output_dir, exist_ok=True)

# Pixabay API (free, no key needed for basic search)
# We'll use direct search and get video URLs

searches = [
    ("trump_politics", "trump US politics white house"),
    ("china_port", "china port belt road shipping"),
    ("oil_tanker", "oil tanker ship strait"),
    ("europe_union", "EU european union flag brussels"),
    ("trade_war", "trade war tariff shipping container"),
    ("global_map", "world map global business"),
    ("factory_asia", "factory asia manufacturing industry"),
    ("business_handshake", "business handshake partnership deal"),
    ("compliance_law", "law document contract compliance"),
    ("growth_chart", "business growth chart data"),
]

pixabay_key = None  # Try without key first

for folder, query in searches:
    dir_path = os.path.join(output_dir, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    # Search Pixabay videos
    url = f"https://pixabay.com/api/videos/?key=&q={query}&per_page=5&safesearch=true"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            for i, video in enumerate(data.get('hits', [])[:3]):
                # Get smallest video
                videos = video.get('videos', {})
                for quality in ['medium', 'small', 'large']:
                    if quality in videos:
                        vurl = videos[quality]['url']
                        vname = f"{folder}_{i+1}.mp4"
                        vpath = os.path.join(dir_path, vname)
                        if not os.path.exists(vpath):
                            print(f"Downloading {vname}...")
                            vresp = requests.get(vurl, timeout=30)
                            with open(vpath, 'wb') as f:
                                f.write(vresp.content)
                            print(f"  Saved {len(vresp.content)} bytes")
                        break
    except Exception as e:
        print(f"Error for {folder}: {e}")

print("Done searching")
