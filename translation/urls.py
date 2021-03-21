from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("translate", views.translateGetImageView, name="translate"),
    path('success', views.success, name = 'success'),
    path("", views.homePageView, name="home"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
