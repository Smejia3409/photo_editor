from PIL import Image, ImageEnhance, ImageFilter
import os
from photo import Photo




# for filename in os.listdir(path):
#     img = Image.open(f"{path}/{filename}")

#     edit = img.filter(ImageFilter.SHARPEN).convert("L")
#     factor = 1.5
#     enhancer = ImageEnhance.Contrast(edit)

#     clean_name = os.path.splitext(filename)[0]
#     edit.save(f".{path_out}/{clean_name}_edited.jpg")


photo = Photo("./imgs", "test.jpeg")

photo.rotate()
