from django.shortcuts import render
from analytics.translator.basic_translation import BasicTranslation

# Create your views here.


def homePageView(request):

    context = {}

    return render(request, "home.html", context)


def translateView(request):

    if request.method == "POST":
        pass

    context = {

    }

    return render(request, "translation.html", context)
