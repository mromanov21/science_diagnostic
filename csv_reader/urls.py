from django.urls import path

from .views import upload_file

app_name = "csv_reader"

urlpatterns = [
    path("", upload_file),
]
