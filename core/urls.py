from django.urls import path
from core.views import ImageUploadView, ResultView


app_name = "core"

urlpatterns = [
    path("", ImageUploadView.as_view(), name="image-upload"),
    path("result-file/<id>/", ResultView.as_view(), name="result-file"),
]