from django.urls import path
from . import views

urlpatterns = [
    path("", views.translateView, name="translate"),
]
