import os
from PIL import Image

FOLDER = r"public\webp"
MAX_WIDTH = 1600
QUALITY = 78

for filename in os.listdir(FOLDER):
    if not filename.lower().endswith('.webp'):
        continue
    filepath = os.path.join(FOLDER, filename)
    img = Image.open(filepath)
    original_mb = os.path.getsize(filepath) / 1024 / 1024

    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.LANCZOS)

    img.save(filepath, 'WEBP', quality=QUALITY)
    new_mb = os.path.getsize(filepath) / 1024 / 1024
    print(f"{filename}: {original_mb:.2f}MB -> {new_mb:.2f}MB")
