from django.shortcuts import render

# Create your views here.


def home(request):
    something = "Page working!"
    return render(request, "home.html", {"something": something})
