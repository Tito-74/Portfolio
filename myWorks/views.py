from django.shortcuts import render
from .models import Works

# Create your views here.

def index(request):
    works = Works.objects.all()
    context = {
        "works": works,
    }
    print("works data", works)
    return render(request, 'index.html', context)


def comments(request):
    return render(request, 'comments.html')