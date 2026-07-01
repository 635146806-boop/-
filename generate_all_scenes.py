#!/usr/bin/env python3
"""Generate ALL scene images using Pillow (guaranteed to render correctly in headless Chrome)"""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATHS = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
]

def find_font():
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

W, H = 1000, 580  # Content frame size

def save(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print(f"Saved {path}")

# ============================================================
# 1. Opening scene - oil strait with dramatic numbers
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(80)
font_mid = get_font(36)
font_small = get_font(20)
font_tiny = get_font(14)

# Big numbers
draw.text((280, 120), "70%", fill='#FFD700', font=font_big, anchor='mt')
draw.text((720, 120), "90%", fill='#FFD700', font=font_big, anchor='mt')
# Descending arrow
draw.polygon([(500, 200), (460, 280), (540, 280)], fill='#FF3366')
draw.rectangle([480, 280, 520, 380], fill='#FF3366')
# Labels
draw.text((500, 420), "霍尔木兹海峡航运量", fill='#FFFFFF', font=font_mid, anchor='mt')
draw.text((500, 460), "断崖式下降", fill='#FF3366', font=font_mid, anchor='mt')
draw.text((500, 520), "数据来源：第十二届走出去风险发布会", fill='#505060', font=font_tiny, anchor='mt')
save(img, 'public/assets/scenes/scene_01_opening.png')

# ============================================================
# 2. Professor Li Haitao
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
# Load professor photo if exists
prof_path = 'public/assets/professor/lihaitao.jpg'
if os.path.exists(prof_path):
    try:
        prof = Image.open(prof_path)
        prof = prof.resize((300, 400), Image.LANCZOS)
        img.paste(prof, (350, 40))
    except:
        pass
    # Name overlay at bottom
    draw.rounded_rectangle([200, 420, 800, 560], radius=10, fill='#000000')
    draw.text((500, 460), "李海涛 教授", fill='#FFD700', font=get_font(40), anchor='mt')
    draw.text((500, 500), "长江商学院院长 · 金融学教授", fill='#FFFFFF', font=get_font(22), anchor='mt')
    draw.text((500, 530), "第十二届中国企业走出去风险发布会", fill='#9090A0', font=get_font(16), anchor='mt')
    save(img, 'public/assets/scenes/scene_02_professor.png')

# ============================================================
# 3. Three risks cards
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_title = get_font(32)
font_header = get_font(20)
font_body = get_font(15)
font_small = get_font(13)

draw.text((W//2, 30), "中国企业出海 · 三大核心风险", fill='#FFFFFF', font=font_title, anchor='mt')

cards = [
    {"x": 25, "color": "#FF3366", "label": "RISK 01", "title": "美国系统性对抗", 
     "items": ["特朗普2026新政", "对华关税升至54%", "300万移民驱逐", "技术封锁升级", "中美经济脱钩"]},
    {"x": 345, "color": "#FFD700", "label": "RISK 02", "title": "政策突变风险",
     "items": ["一夜之间政策变卦", "印尼镍矿出口禁令", "印度封禁中国APP", "越南反倾销调查", "沙特本地化要求"]},
    {"x": 665, "color": "#00FF88", "label": "RISK 03", "title": "欧盟潜在风险",
     "items": ["最大贸易顺差来源", "反补贴调查启动", "碳边境调节机制", "新能源车关税", "海外建厂策略"]},
]

for c in cards:
    x, color = c["x"], c["color"]
    draw.rounded_rectangle([x, 65, x+310, 530], radius=10, fill='#111118', outline=color, width=2)
    draw.rounded_rectangle([x, 65, x+310, 73], radius=4, fill=color)
    draw.text((x+155, 90), c["label"], fill=color, font=font_small, anchor='mt')
    draw.text((x+155, 120), c["title"], fill='#FFFFFF', font=font_header, anchor='mt')
    draw.line([(x+20, 150), (x+290, 150)], fill=color, width=1)
    for i, item in enumerate(c["items"]):
        prefix = "• " if i > 0 else "▸ "
        draw.text((x+25, 175 + i*30), prefix + item, fill='#C0C0D0', font=font_body, anchor='lt')

draw.text((W//2, 555), "数据来源：第十二届中国企业走出去风险发布会", fill='#505060', font=font_small, anchor='mt')
save(img, 'public/assets/scenes/scene_03_three_risks.png')

# ============================================================
# 4. US Confrontation
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_title = get_font(26)
font_header = get_font(19)
font_body = get_font(15)
font_small = get_font(13)
font_vs = get_font(17)

draw.rounded_rectangle([0, 0, W, 48], radius=0, fill='#1a1020')
draw.text((W//2, 28), "美国系统性对抗 — 全球博弈格局", fill='#FF3366', font=font_title, anchor='mt')

draw.rounded_rectangle([350, 55, 650, 220], radius=8, fill='#0d0d1a', outline='#FF3366', width=2)
draw.text((500, 85), "美国", fill='#FFFFFF', font=font_header, anchor='mt')
draw.text((500, 115), "系统性对抗中心", fill='#FF3366', font=font_body, anchor='mt')
draw.text((500, 145), "关税54% · 技术封锁 · 经济脱钩", fill='#9090A0', font=font_small, anchor='mt')
draw.text((500, 170), "移民驱逐 · 供应链重构", fill='#9090A0', font=font_small, anchor='mt')

draw.text((175, 240), "VS", fill='#FF3366', font=font_vs, anchor='mt')
draw.text((500, 240), "VS", fill='#FF3366', font=font_vs, anchor='mt')
draw.text((825, 240), "VS", fill='#FF3366', font=font_vs, anchor='mt')

targets = [
    {"x": 25, "name": "委内瑞拉", "items": ["石油制裁", "金融封锁", "转口枢纽受阻"]},
    {"x": 350, "name": "古巴", "items": ["长期禁运", "旅游限制", "中古经贸受阻"]},
    {"x": 675, "name": "霍尔木兹", "items": ["军事威慑", "航运威胁", "70-90%下降"]},
]

for t in targets:
    x = t["x"]
    draw.rounded_rectangle([x, 265, x+300, 410], radius=8, fill='#0d0d1a', outline='#FFD700', width=1)
    draw.text((x+150, 295), t["name"], fill='#FFD700', font=font_header, anchor='mt')
    for i, item in enumerate(t["items"]):
        draw.text((x+25, 325 + i*26), "• " + item, fill='#A0A0B0', font=font_small, anchor='lt')

draw.rounded_rectangle([60, 430, 940, 480], radius=6, fill='#1a1020', outline='#FF3366', width=1)
draw.text((500, 460), "→ 重新评估全球供应链布局，寻找替代路径与区域合作新方案", fill='#FF3366', font=font_small, anchor='mt')

stats = [("受影响国家", "20+", "#FF3366"), ("关税增幅", "54%", "#FFD700"), ("航运下降", "70-90%", "#00FF88")]
for i, (label, val, col) in enumerate(stats):
    x = 80 + i * 310
    draw.rounded_rectangle([x, 500, x+280, 565], radius=4, fill='#0d0d1a')
    draw.text((x+140, 520), label, fill='#9090A0', font=font_small, anchor='mt')
    draw.text((x+140, 550), val, fill=col, font=font_header, anchor='mt')

save(img, 'public/assets/scenes/scene_04_us_confrontation.png')

# ============================================================
# 5. Belt and Road / Global South
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(48)
font_mid = get_font(24)
font_small = get_font(16)

# Draw a simple belt/road map representation
draw.text((W//2, 60), "一带一路 · 全球南方", fill='#00FF88', font=font_big, anchor='mt')
# China dot
draw.ellipse([200, 150, 240, 190], fill='#FF3366')
draw.text((220, 200), "中国", fill='#FFFFFF', font=font_mid, anchor='mt')
# Road line
draw.line([(240, 170), (400, 170)], fill='#00FF88', width=3)
# Venezuela
draw.ellipse([400, 150, 440, 190], fill='#FFD700')
draw.text((420, 200), "委内瑞拉", fill='#FFFFFF', font=font_mid, anchor='mt')
# Road line
draw.line([(440, 170), (600, 170)], fill='#00FF88', width=3)
# Cuba
draw.ellipse([600, 150, 640, 190], fill='#FFD700')
draw.text((620, 200), "古巴", fill='#FFFFFF', font=font_mid, anchor='mt')
# Road line
draw.line([(640, 170), (800, 170)], fill='#00FF88', width=3)
# Hormuz
draw.ellipse([800, 150, 840, 190], fill='#00FF88')
draw.text((820, 200), "霍尔木兹", fill='#FFFFFF', font=font_mid, anchor='mt')

# Bottom description
draw.text((W//2, 300), "转口贸易路径 · 全球南方市场 · 区域供应链重构", fill='#9090A0', font=font_mid, anchor='mt')
draw.text((W//2, 340), "中国企业出海新机遇", fill='#00FF88', font=get_font(32), anchor='mt')

# Stats
draw.text((W//2, 450), "受影响国家: 20+  |  关键海峡: 霍尔木兹  |  新兴市场: 全球南方", fill='#606070', font=font_small, anchor='mt')
save(img, 'public/assets/scenes/scene_05_belt_road.png')

# ============================================================
# 6. Hormuz 70-90% (reuses scene_01)
# ============================================================
# Same as opening scene
save(img.copy(), 'public/assets/scenes/scene_06_hormuz.png')

# ============================================================
# 7. Policy change - will use real video, no image needed
# ============================================================
# Skip - uses video asset

# ============================================================
# 8. Five nations policy cases
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(36)
font_mid = get_font(20)
font_small = get_font(15)

draw.text((W//2, 40), "政策突变案例", fill='#FF3366', font=font_big, anchor='mt')
draw.text((W//2, 80), "一夜之间政策变卦", fill='#B0B0C0', font=font_mid, anchor='mt')

nations = [
    {"x": 50, "name": "印尼", "color": "#FF3366", "policy": "镍矿出口禁令", "year": "2020"},
    {"x": 220, "name": "印度", "color": "#FFD700", "policy": "封禁中国APP", "year": "2020"},
    {"x": 390, "name": "越南", "color": "#00FF88", "policy": "反倾销调查", "year": "2021"},
    {"x": 560, "name": "沙特", "color": "#FF3366", "policy": "本地化要求", "year": "2023"},
    {"x": 730, "name": "非洲", "color": "#FFD700", "policy": "多项政策调整", "year": "持续"},
]

for n in nations:
    x = n["x"]
    draw.rounded_rectangle([x, 120, x+160, 350], radius=8, fill='#111118', outline=n["color"], width=2)
    draw.rounded_rectangle([x, 120, x+160, 128], radius=4, fill=n["color"])
    draw.text((x+80, 150), n["name"], fill='#FFFFFF', font=font_mid, anchor='mt')
    draw.text((x+80, 190), n["policy"], fill=n["color"], font=font_small, anchor='mt')
    draw.text((x+80, 220), n["year"], fill='#606070', font=font_small, anchor='mt')
    # Flag placeholder - just colored circle
    draw.ellipse([x+60, 260, x+100, 300], fill=n["color"])

# Impact
draw.rounded_rectangle([50, 380, 950, 440], radius=6, fill='#1a1020', outline='#FF3366', width=1)
draw.text((500, 415), "→ 提前政治尽调 · 多元化布局 · 应急预案机制", fill='#FF3366', font=font_mid, anchor='mt')

# Bottom note
draw.text((W//2, 500), "合规是门票，不是成本", fill='#00FF88', font=get_font(28), anchor='mt')
save(img, 'public/assets/scenes/scene_08_five_nations.png')

# ============================================================
# 9. EU Risk
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(40)
font_mid = get_font(22)
font_small = get_font(16)

draw.text((W//2, 50), "欧盟潜在风险", fill='#FFD700', font=font_big, anchor='mt')
draw.text((W//2, 100), "最大贸易顺差来源 · 关税冲击", fill='#B0B0C0', font=font_mid, anchor='mt')

# EU circle
draw.ellipse([400, 160, 600, 360], fill='#0d0d1a', outline='#FFD700', width=3)
draw.text((500, 260), "EU", fill='#FFD700', font=get_font(60), anchor='mt')

# Risk items
risks = ["反补贴调查启动", "碳边境调节机制", "新能源车关税", "海外建厂策略", "绿色合规体系"]
for i, r in enumerate(risks):
    draw.text((W//2, 390 + i*30), "• " + r, fill='#C0C0D0', font=font_small, anchor='mt')

save(img, 'public/assets/scenes/scene_09_eu_risk.png')

# ============================================================
# 10. Three responses - uses video
# ============================================================
# Skip - uses video asset

# ============================================================
# 11. Geopolitical insight
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(42)
font_mid = get_font(24)
font_small = get_font(18)

draw.text((W//2, 60), "地缘洞察能力", fill='#FFD700', font=font_big, anchor='mt')
draw.text((W//2, 120), "不能只算经济账，不算政治账", fill='#B0B0C0', font=font_mid, anchor='mt')

# Globe representation
draw.ellipse([350, 180, 650, 420], fill='#0d0d1a', outline='#00FF88', width=3)
draw.arc([350, 180, 650, 420], start=0, end=180, fill='#00FF88', width=2)
draw.arc([350, 180, 650, 420], start=90, end=270, fill='#00FF88', width=2)
draw.text((500, 300), "全球", fill='#00FF88', font=get_font(48), anchor='mt')

# Key points
points = ["政治尽调优先", "地缘风险评估", "多国布局策略", "应急预案准备"]
for i, p in enumerate(points):
    draw.text((W//2, 450 + i*28), "▸ " + p, fill='#C0C0D0', font=font_small, anchor='mt')

save(img, 'public/assets/scenes/scene_11_geopolitical.png')

# ============================================================
# 12. Compliance
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(42)
font_mid = get_font(24)
font_small = get_font(18)

draw.text((W//2, 60), "合规能力", fill='#00FF88', font=font_big, anchor='mt')
draw.text((W//2, 120), "合规是门票，不是成本", fill='#B0B0C0', font=font_mid, anchor='mt')

# Gate representation
draw.rounded_rectangle([300, 180, 700, 400], radius=10, fill='#0d0d1a', outline='#00FF88', width=3)
draw.text((500, 290), "合规", fill='#00FF88', font=get_font(60), anchor='mt')
draw.text((500, 360), "COMPLIANCE", fill='#00FF88', font=font_small, anchor='mt')

# Key points
points = ["法律合规审查", "税务合规体系", "数据合规保护", "ESG合规标准"]
for i, p in enumerate(points):
    draw.text((W//2, 430 + i*28), "▸ " + p, fill='#C0C0D0', font=font_small, anchor='mt')

save(img, 'public/assets/scenes/scene_12_compliance.png')

# ============================================================
# 13. Localization - uses video
# ============================================================
# Skip - uses video

# ============================================================
# 14. Win-win handshake
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(38)
font_mid = get_font(22)
font_small = get_font(16)

draw.text((W//2, 50), "走进去才能走出来", fill='#FFD700', font=font_big, anchor='mt')
draw.text((W//2, 100), "深入当地 · 扎根当地 · 与当地共赢", fill='#B0B0C0', font=font_mid, anchor='mt')

# Two hands shaking representation
draw.rounded_rectangle([200, 160, 480, 380], radius=10, fill='#0d0d1a', outline='#00FF88', width=2)
draw.text((340, 270), "中国", fill='#00FF88', font=get_font(36), anchor='mt')

draw.rounded_rectangle([520, 160, 800, 380], radius=10, fill='#0d0d1a', outline='#FFD700', width=2)
draw.text((660, 270), "当地", fill='#FFD700', font=get_font(36), anchor='mt')

# Connection
draw.line([(480, 270), (520, 270)], fill='#00FF88', width=4)
draw.polygon([(500, 260), (500, 280), (520, 270)], fill='#00FF88')

# Benefits
benefits = ["本地化运营", "文化融合", "人才本土化", "供应链协同"]
for i, b in enumerate(benefits):
    draw.text((W//2, 420 + i*26), "▸ " + b, fill='#C0C0D0', font=font_small, anchor='mt')

save(img, 'public/assets/scenes/scene_14_handshake.png')

# ============================================================
# 15. Growth opportunity - uses video
# ============================================================
# Skip - uses video

# ============================================================
# 16. Final CTA
# ============================================================
img = Image.new('RGB', (W, H), '#0A0A0F')
draw = ImageDraw.Draw(img)
font_big = get_font(44)
font_mid = get_font(24)
font_small = get_font(18)

draw.text((W//2, 60), "抓住机遇 · 管控风险", fill='#00FF88', font=font_big, anchor='mt')
draw.text((W//2, 120), "逆势上扬 · 中国企业出海新格局", fill='#B0B0C0', font=font_mid, anchor='mt')

# Up arrow
draw.polygon([(500, 200), (420, 320), (580, 320)], fill='#00FF88')
draw.rectangle([480, 320, 520, 420], fill='#00FF88')

# Stats
stats = ["出口逆势上扬", "风险不断涌现", "机遇与挑战并存"]
for i, s in enumerate(stats):
    draw.text((W//2, 450 + i*28), "▸ " + s, fill='#C0C0D0', font=font_small, anchor='mt')

save(img, 'public/assets/scenes/scene_16_final.png')

print("\n=== All scene images generated successfully ===")
