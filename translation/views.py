from django.shortcuts import render

# Create your views here.


def translateView(request):
    context = {

    }

    return render(request, "translation.html", context)
