from django.shortcuts import render

# Create your views here.


def translateView(request):
    context = {

    }

    return render(request, "home.html", context)
