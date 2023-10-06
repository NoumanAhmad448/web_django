from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_url, name="index"),
    path("test", views.main_url, name="index1"),
]