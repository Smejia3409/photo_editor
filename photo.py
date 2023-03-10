from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os


def temp_save(filename, img):
    clean_name = os.path.splitext(filename)[0]
    # print(f"./editedImgs/{clean_name}.jpeg")
    img.save(f"../editedImgs/{clean_name}.jpeg")

# gets file clean file name


def clean_name(filename):
    clean_name = os.path.splitext(filename)[0]
    return clean_name


class Photo():
    def __init__(self, path, filename):
        # self.path = path
        # self.filename = filename

        # edited = Image.open(
        #     f"./editedImgs/{os.path.splitext(filename)[0]}_editied.jpeg")

        # logic setup for path and filename
        if os.path.isfile(f"../editedImgs/{os.path.splitext(filename)[0]}.jpeg"):

            self.path = "../editedImgs"
            self.filename = f"{clean_name(filename)}.jpeg"
            self.img = Image.open(f"{self.path}/{self.filename}")

            print("file found in edited")

        else:
            self.path = path
            self.filename = filename
            self.img = Image.open(f"{path}/{filename}")

            print("img not found")

    def sharpen(self):
        print(self.path)
        edit = self.img.filter(ImageFilter.SHARPEN)
        temp_save(self.filename, edit)
        print(self.filename + ":sharpened")

    # blurs image
    def blur(self):
        print(self.path)
        edit = self.img.filter(ImageFilter.BLUR)
        temp_save(self.filename, edit)
        print(self.filename + ":Blur")

    # turns image to greyscale
    def greyscale(self):
        print(self.path)
        edit = self.img.convert("L")
        print(self.filename + ":Greyscale")
        temp_save(self.filename, edit)

    # clockwise rotation
    def rotate_cw(self):
        print(self.path)
        edit = self.img.rotate(-90)
        temp_save(self.filename, edit)
        print(self.filename + ":rotated")

    # counter clockwise
    def rotate_cc(self):
        edit = self.img.rotate(90)
        temp_save(self.filename, edit)
        print(self.filename + ":counter clockwise")


    def mirror(self):
        edit = ImageOps.mirror(self.img)
        temp_save(self.filename, edit)
        print(self.filename + ":Mirror")

