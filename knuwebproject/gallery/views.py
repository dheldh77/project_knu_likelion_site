from django.shortcuts import render
from .models import Gallery

# Create your views here.
def board(request):
    galleries = Gallery.objects
    return render(request,"gallery.html", {'galleries':galleries})