from pathlib import Path

from PIL import Image


ASSET_DIR = Path(__file__).resolve().parent
image = Image.open(ASSET_DIR / "app_logo.png").convert("RGBA")

image.save(
    ASSET_DIR / "app_icon.ico",
    format="ICO",
    sizes=((16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)),
)
