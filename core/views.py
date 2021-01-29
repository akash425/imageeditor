import os
from PIL import Image, ImageOps

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import ListView, UpdateView
from django.conf import settings

from core.forms import ImageUploadForm
from core.models import TempImage


class ImageUploadView(View):
    template_name = "forms.html"
    form_class = ImageUploadForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            operation_type = form.cleaned_data["operation_type"]
            del form.cleaned_data["operation_type"]
            image = TempImage.objects.create(**form.cleaned_data)
            image.perform_operation(int(operation_type))
            return redirect(reverse("core:result-file", kwargs={"id": image.id}))
        return render(request, self.template_name, {"form": form})


class ResultView(View):
    template_name = "result.html"

    def get(self, request, id):
        image = TempImage.objects.get(pk=id)
        context = {
            "original_file": image.image_file.url,
            "result_file": image.result_file.url,
        }
        return render(request, self.template_name, context)
