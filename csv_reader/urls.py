from django.urls import path

from .views import answers_and_users, upload_file

app_name = "csv_reader"

urlpatterns = [
    path("", upload_file, name="index"),
    path("user_answers/", answers_and_users, name="answers"),
]
