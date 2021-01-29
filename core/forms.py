from django import forms
from core.models import TempImage

IMAGE_OPERATION_TYPE = (
    (1, "Greyscale"),
    (2, "Flip"),
    (3, "Mirror"),
    (4, "Crop"),
    (5, "Resize"),
    (6, "Rotate"),
    (7, "Resize and Compress")
)


class ImageUploadForm(forms.Form):
    image_file = forms.ImageField()
    operation_type = forms.ChoiceField(choices=IMAGE_OPERATION_TYPE)
