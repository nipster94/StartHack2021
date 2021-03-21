from django.db import models


# Create your models here.
class TranslationGetImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    request_language = models.CharField(max_length=100)
    # translation_text = models.TextField()
    # summary = models.TextField()

class TranslateImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    # request_language = models.CharField(max_length=100)
    translation_text = models.TextField()
    summary = models.TextField()
