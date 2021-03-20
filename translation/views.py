from django.shortcuts import render
from analytics.translator.basic_translation import BasicTranslation

# Create your views here.


def translateView(request):
    context = {

    }

    return render(request, "translation.html", context)
