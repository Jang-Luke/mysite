from django.urls import path

from . import views

urlpatterns = [
    path("", views.scrap, name="scrap"),
    path("<str:melon>", views.scrap, name="scrap2"),
]