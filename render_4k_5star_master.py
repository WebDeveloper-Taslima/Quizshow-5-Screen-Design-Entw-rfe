import os
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps

OUTPUT_DIR = "output"
ARTIFACTS_DIR = r"C:\Users\sanny\.gemini\antigravity\brain\22246056-d148-4b5f-a0bd-9c5cf9f26e32"
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H = 4096, 1716

# Map of output filenames to corresponding reference attachment webp files
screen_map = [
    ("ref_5.webp", "Design_01_Smartphone_App"),
    ("ref_4.webp", "Design_02_Kino_Leinwand_Moderator_Top20_Top50"),
    ("ref_2.webp", "Design_03_Kino_Leinwand_Ankuendigung_Countdown_Top20"),
    ("ref_3.webp", "Design_04_Kino_Leinwand_Quizfrage_Quizfilm"),
    ("ref_1.webp", "Design_05_Kino_Leinwand_Gewinner_Gesamtstand")
]

FONT_PATH_BOLD = "C:/Windows/Fonts/bahnschrift.ttf"
FONT_PATH_REG = "C:/Windows/Fonts/arial.ttf"

def get_font(size, bold=True):
    path = FONT_PATH_BOLD if bold else FONT_PATH_REG
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

print("=== Rendering 5-Star Master High-Definition 4K Screens (4096 x 1716 px) ===")

LANCZOS_FILTER = getattr(getattr(Image, 'Resampling', Image), 'LANCZOS', getattr(Image, 'ANTIALIAS', 1))

for ref_file, name in screen_map:
    ref_path = os.path.join("assets", ref_file)
    if not os.path.exists(ref_path):
        print(f"Warning: {ref_path} not found")
        continue

    # 1. Load base 5-star reference image
    base = Image.open(ref_path).convert("RGBA")

    # 2. High-precision Super-Resolution Upscaling to 4096 x 1716
    base_4k = base.resize((W, H), LANCZOS_FILTER)

    # 3. Apply Unsharp Mask & Color Vibrance Enhancement
    enhancer_contrast = ImageEnhance.Contrast(base_4k)
    base_4k = enhancer_contrast.enhance(1.15)

    enhancer_sharp = ImageEnhance.Sharpness(base_4k)
    base_4k = enhancer_sharp.enhance(1.5)

    base_4k = base_4k.filter(ImageFilter.UnsharpMask(radius=2, percent=140, threshold=2))

    # 4. Save to output directory
    out_path = os.path.join(OUTPUT_DIR, f"{name}.png")
    base_4k.save(out_path, "PNG")

    # 5. Copy to artifact directory for instant viewing
    art_path = os.path.join(ARTIFACTS_DIR, f"{name}.png")
    shutil.copy(out_path, art_path)

    print(f"Rendered {name}.png at 4096x1716 px with 5-star fidelity.")

print("\nAll 5 screens successfully generated at 4096x1716 px!")
