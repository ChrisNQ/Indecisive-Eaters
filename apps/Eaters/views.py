from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Eaters/index.html")

def add(request):
    pass

def favorites(request):
    return render(request, "Eaters/favorites.html")
