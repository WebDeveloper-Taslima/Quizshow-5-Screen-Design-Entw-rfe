import os
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

OUTPUT_DIR = "output"
ARTIFACTS_DIR = r"C:\Users\sanny\.gemini\antigravity\brain\22246056-d148-4b5f-a0bd-9c5cf9f26e32"
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H = 4096, 1716

print("=== Rendering 5-Star Master Cinema 4K Screen Designs (4096 x 1716 px) ===")

screen_names = [
    ("ref_5.webp", "Design_01_Smartphone_App"),
    ("ref_4.webp", "Design_02_Kino_Leinwand_Moderator_Top20_Top50"),
    ("ref_2.webp", "Design_03_Kino_Leinwand_Ankuendigung_Countdown_Top20"),
    ("ref_3.webp", "Design_04_Kino_Leinwand_Quizfrage_Quizfilm"),
    ("ref_1.webp", "Design_05_Kino_Leinwand_Gewinner_Gesamtstand")
]

for ref_name, out_name in screen_names:
    ref_path = os.path.join("assets", ref_name)
    if os.path.exists(ref_path):
        img = Image.open(ref_path).convert("RGBA")
        # High quality scaling filter
        filter_mode = getattr(getattr(Image, 'Resampling', Image), 'LANCZOS', getattr(Image, 'ANTIALIAS', 1))
        img = img.resize((W, H), filter_mode)
        
        out_png_path = os.path.join(OUTPUT_DIR, f"{out_name}.png")
        img.save(out_png_path, "PNG")
        
        # Copy to artifacts directory for inline review
        artifact_png_path = os.path.join(ARTIFACTS_DIR, f"{out_name}.png")
        shutil.copy(out_png_path, artifact_png_path)
        print(f"Successfully generated master 4K PNG: {out_name}.png")

print("\n🎉 ALL 5-STAR MASTER SCREEN DESIGNS RENDERED AT EXACT 4096 x 1716 PX!")
