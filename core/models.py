import os
from PIL import Image, ImageOps

from django.db import models
from django.conf import settings

from utils.image_ops import ImageOperations


class TempImage(models.Model):
    image_file = models.ImageField(upload_to="temp/")
    result_file = models.ImageField(upload_to="results/", blank=True, null=True)

    def perform_operation(self, operation_type):
        image_operations = ImageOperations(self.image_file.path, operation_type)
        self.result_file = image_operations.perform_operation()
        self.save()
