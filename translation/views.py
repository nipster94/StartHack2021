import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from .forms import TranslationForm, TranslationResultsForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from analytics.translator.basic_translation import BasicTranslation
from analytics.vision.vision_main import AnalyzeDocument
from django.conf import settings

_name = ""


# Create your views here.
def translateGetImageView(request):
    if request.method == "POST":
        form = TranslationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TranslationForm()
    return render(request, 'translation.html', {'form': form})


def success(request):
    vision_analysis = AnalyzeDocument()
    print(settings.BASE_DIR)
    vision_analysis.authentication(settings.BASE_DIR)

    image = open(settings.MEDIA_ROOT + '/images/de-OP-Bericht-001.jpeg', "rb")
    translated_text_ = vision_analysis.azure_ocr_image(image, 'en')
    # translated_text_ = "Test text"

    context = {
        'traslated_text': translated_text_,
        'summary': "This is s summary"
    }

    # print(translated_text_)
    # return HttpResponse('successfully uploaded')

    # form_result = TranslationResultsForm()
    # # form_result.instance.image = image
    # # form_result.instance.translation_text = translated_text_
    # # form_result.instance.summary = "This is a summary"
    # form_result.image = image
    # form_result.translation_text = translated_text_
    # form_result.summary = "This is a summary"

    return render(request, 'translation_results.html', context)
    # return render(request, 'translation_results.html',{'form': form_result})
