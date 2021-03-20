from django.urls import path
from . import views

urlpatterns = [
    path("translate", views.translateView, name="translation"),
    path("", views.homePageView, name="home"),
]
