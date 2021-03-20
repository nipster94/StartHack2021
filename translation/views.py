from django.shortcuts import render
from analytics.translator.basic_translation import BasicTranslation

# Create your views here.


def translateView(request):

    if request.method == "POST":
        pass

    context = {

    }

    return render(request, "translation.html", context)
