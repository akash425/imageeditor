import os
from datetime import date

from PIL import Image, ImageOps

from django.conf import settings


class ImageOperations:

    def __init__(self, image_path, operation_type):
        self.image_path = image_path
        self.operation_type = operation_type

    def open_image(self, image_path):
        return Image.open(image_path)

    def perform_operation(self, i=date.today()):
        image_file = self.open_image(self.image_path)
        filename, extension = os.path.splitext(self.image_path)
        # filename = filename.split("/")[-1]
        if self.operation_type == 1:
            image_file = self.perform_grayscale(image_file)
        elif self.operation_type == 2:
            image_file = self.perform_flip(image_file)
        elif self.operation_type == 3:
            image_file = self.perform_mirror(image_file)
        elif self.operation_type == 4:
            image_file = self.perform_crop(image_file)
        elif self.operation_type == 5:
            image_file = self.perform_resize(image_file)
        elif self.operation_type == 6:
            image_file = self.perform_rotate(image_file)
        elif self.operation_type == 7:
            image_file = self.perform_fit(image_file)
        outfile = f"{i}result{extension}"
        image_file.save(f"{settings.MEDIA_ROOT}/{outfile}")
        return outfile

    @staticmethod
    def perform_flip(image_file):
        return ImageOps.flip(image_file)

    @staticmethod
    def perform_grayscale(image_file):
        return ImageOps.grayscale(image_file)

    @staticmethod
    def perform_mirror(image_file):
        return ImageOps.mirror(image_file)

    @staticmethod
    def perform_crop(image_file):
        width, height = image_file.size

        # l = int(height * 0.2)
        l = width * 0.2
        t = height * 0.2
        r = width * 0.8
        b = height * 0.8
        cf = image_file.crop((l, t, r, b))
        return cf

    @staticmethod
    def perform_fit(image_file):
        width, height = image_file.size
        w = int(width/1.5)
        h = int(height/1.5)
        return ImageOps.fit(image_file, (w, h), method=0,
                            bleed=0.0, centering=(0.05, 0.05))

    @staticmethod
    def perform_resize(image_file):
        return ImageOps.crop(image_file)

    @staticmethod
    def perform_rotate(image_file):
        return Image.Image.rotate(image_file, 90)
