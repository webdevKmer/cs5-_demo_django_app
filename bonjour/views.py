from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'bonjour/index.html', context)

def hello_name(request, name):
    context = {
        "name": name.capitalize()
    }
    return render(request, 'bonjour/index.html', context)