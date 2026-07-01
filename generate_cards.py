#!/usr/bin/env python3
"""Generate high-quality card images using Pillow (guaranteed to render correctly)"""
from PIL import Image, ImageDraw, ImageFont
import os

# Try to find a good CJK font
FONT_PATHS = [
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
]

def find_font():
    for p in FONT_PATHS:
        if os.path.exists(p):
            return p
    # Try to install noto fonts
    os.system("apt-get update -qq && apt-get install -y -qq fonts-noto-cjk 2>/dev/null")
    for p in FONT_PATHS:
        if os.path.exists(p):
            return p
    return None

FONT_PATH = find_font()
print(f"Font: {FONT_PATH}")

def get_font(size):
    if FONT_PATH:
        try:
            return ImageFont.truetype(FONT_PATH, size)
        except:
            pass
    return ImageFont.load_default()

W, H = 1000, 580

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def make_three_risks():
    img = Image.new('RGB', (W, H), '#0A0A0F')
    draw = ImageDraw.Draw(img)
    
    font_title = get_font(36)
    font_header = get_font(22)
    font_body = get_font(16)
    font_small = get_font(14)
    
    # Title
    draw.text((W//2, 30), "中国企业出海 · 三大核心风险", fill='#FFFFFF', font=font_title, anchor='mt')
    
    cards = [
        {"x": 30, "color": "#FF3366", "label": "RISK 01", "title": "美国系统性对抗", 
         "items": ["特朗普2026新政", "对华关税升至54%", "300万移民驱逐", "技术封锁升级", "中美经济脱钩"]},
        {"x": 350, "color": "#FFD700", "label": "RISK 02", "title": "政策突变风险",
         "items": ["一夜之间政策变卦", "印尼镍矿出口禁令", "印度封禁中国APP", "越南反倾销调查", "沙特本地化要求"]},
        {"x": 670, "color": "#00FF88", "label": "RISK 03", "title": "欧盟潜在风险",
         "items": ["最大贸易顺差来源", "反补贴调查启动", "碳边境调节机制", "新能源车关税", "海外建厂策略"]},
    ]
    
    for c in cards:
        x, color = c["x"], c["color"]
        # Card bg
        draw.rounded_rectangle([x, 70, x+300, 540], radius=10, fill='#111118', outline=color, width=2)
        # Top accent bar
        draw.rounded_rectangle([x, 70, x+300, 78], radius=4, fill=color)
        # Label
        draw.text((x+150, 95), c["label"], fill=color, font=font_small, anchor='mt')
        # Title
        draw.text((x+150, 130), c["title"], fill='#FFFFFF', font=font_header, anchor='mt')
        # Divider
        draw.line([(x+30, 160), (x+270, 160)], fill=color, width=1)
        # Items
        for i, item in enumerate(c["items"]):
            prefix = "• " if i > 0 else "▸ "
            draw.text((x+30, 185 + i*32), prefix + item, fill='#C0C0D0', font=font_body, anchor='lt')
    
    # Bottom source
    draw.text((W//2, 555), "数据来源：第十二届中国企业走出去风险发布会", fill='#505060', font=font_small, anchor='mt')
    
    img.save('/workspace/demo_video/chuhai-fenxian/public/assets/three_risks/three_risks_v2.png')
    print("Saved three_risks_v2.png")

def make_us_confrontation():
    img = Image.new('RGB', (W, H), '#0A0A0F')
    draw = ImageDraw.Draw(img)
    
    font_title = get_font(28)
    font_header = get_font(20)
    font_body = get_font(16)
    font_small = get_font(14)
    font_vs = get_font(18)
    
    # Title bar
    draw.rounded_rectangle([0, 0, W, 50], radius=0, fill='#1a1020')
    draw.text((W//2, 28), "美国系统性对抗 — 全球博弈格局", fill='#FF3366', font=font_title, anchor='mt')
    
    # US Center card
    draw.rounded_rectangle([350, 60, 650, 240], radius=8, fill='#0d0d1a', outline='#FF3366', width=2)
    draw.text((500, 95), "美国", fill='#FFFFFF', font=font_header, anchor='mt')
    draw.text((500, 125), "系统性对抗中心", fill='#FF3366', font=font_body, anchor='mt')
    draw.text((500, 155), "关税54% · 技术封锁 · 经济脱钩", fill='#9090A0', font=font_small, anchor='mt')
    draw.text((500, 180), "移民驱逐 · 供应链重构", fill='#9090A0', font=font_small, anchor='mt')
    
    # VS lines and badges (simplified as text)
    draw.text((175, 255), "VS", fill='#FF3366', font=font_vs, anchor='mt')
    draw.text((500, 255), "VS", fill='#FF3366', font=font_vs, anchor='mt')
    draw.text((825, 255), "VS", fill='#FF3366', font=font_vs, anchor='mt')
    
    # Target cards
    targets = [
        {"x": 30, "name": "委内瑞拉", "items": ["石油制裁", "金融封锁", "转口枢纽受阻"]},
        {"x": 350, "name": "古巴", "items": ["长期禁运", "旅游限制", "中古经贸受阻"]},
        {"x": 670, "name": "霍尔木兹", "items": ["军事威慑", "航运威胁", "70-90%下降"]},
    ]
    
    for t in targets:
        x = t["x"]
        draw.rounded_rectangle([x, 280, x+300, 430], radius=8, fill='#0d0d1a', outline='#FFD700', width=1)
        draw.text((x+150, 310), t["name"], fill='#FFD700', font=font_header, anchor='mt')
        for i, item in enumerate(t["items"]):
            draw.text((x+30, 345 + i*28), "• " + item, fill='#A0A0B0', font=font_small, anchor='lt')
    
    # Impact bar
    draw.rounded_rectangle([60, 460, 940, 510], radius=6, fill='#1a1020', outline='#FF3366', width=1)
    draw.text((500, 490), "→ 重新评估全球供应链布局，寻找替代路径与区域合作新方案", fill='#FF3366', font=font_small, anchor='mt')
    
    # Stats
    stats = [("受影响国家", "20+", "#FF3366"), ("关税增幅", "54%", "#FFD700"), ("航运下降", "70-90%", "#00FF88")]
    for i, (label, val, col) in enumerate(stats):
        x = 80 + i * 310
        draw.rounded_rectangle([x, 530, x+280, 575], radius=4, fill='#0d0d1a')
        draw.text((x+140, 545), label, fill='#9090A0', font=font_small, anchor='mt')
        draw.text((x+140, 568), val, fill=col, font=font_header, anchor='mt')
    
    img.save('/workspace/demo_video/chuhai-fenxian/public/assets/us_confrontation/us_confrontation_v2.png')
    print("Saved us_confrontation_v2.png")

if __name__ == '__main__':
    make_three_risks()
    make_us_confrontation()
