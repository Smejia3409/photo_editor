from PIL import Image, ImageEnhance, ImageFilter
import os


def save_photo(filename, img):
    clean_name = os.path.splitext(filename)[0]
    img.save(f"./editedImgs/{clean_name}_edited.jpeg")


class Photo():
    def __init__(self, path, filename):
        # self.path = path
        # self.filename = filename
        self.img = Image.open(f"{path}/{filename}")
        # edited = Image.open(
        #     f"./editedImgs/{os.path.splitext(filename)[0]}_editied.jpeg")

        # logic setup for path and filename
        if not os.path.isfile(f"./editedImgs/{os.path.splitext(filename)[0]}_editied.jpeg"):

            self.path = "./editedImgs"
            self.filename = f"{filename}_editied.jpeg"
            print("file found in edited")
        else:
            self.path = path
            self.filename = filename

    def sharpen(self):
        edit = self.img.filter(ImageFilter.SHARPEN)
        save_photo(self.filename, edit)
        print(self.filename + ":sharpened")

    def greyscale(self):
        edit = self.img.convert("L")
        clean_name = os.path.splitext(self.filename)[0]
        edit.save(f"./editedImgs/{clean_name}_editied.jpeg")

    def rotate(self):
        edit = self.img.rotate(-90)
        save_photo(self.filename, edit)
        print(self.filename + ":rotated")
