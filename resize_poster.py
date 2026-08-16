from PIL import Image
import os

path = r"public\Resources\Images\Posters\BotakiMontage.mp4"  # adjust filename/extension
img = Image.open(path)

# Resize so the longest side is max 2500px (posters don't need to be huge)
max_dim = 2500
ratio = max_dim / max(img.size)
if ratio < 1:
    new_size = (int(img.size[0]*ratio), int(img.size[1]*ratio))
    img = img.resize(new_size, Image.LANCZOS)

img.save(path, quality=80, optimize=True)
print(f"New size: {os.path.getsize(path)/1024/1024:.2f} MB")