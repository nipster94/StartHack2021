from django import forms
from .models import *

class TranslationForm(forms.ModelForm):
    class Meta:
        model = TranslationGetImageModel
        fields = ['image', 'request_language']
        # fields = ['image', 'translation_text','summary']

class TranslationResultsForm(forms.ModelForm):
    class Meta:
        model = TranslateImageModel
        fields = ['image', 'translation_text','summary']
