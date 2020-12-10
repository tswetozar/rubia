from django.shortcuts import render


# Create your views here.

def index(request):
    x = 6
    return render(request, 'index.html')
