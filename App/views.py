from django.shortcuts import render
from .models import Author


# Create your views here.
def all(request):
    req = Author.objects.all()
    return render(request, 'app/index.html', {'req': req})
