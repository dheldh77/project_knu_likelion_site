from django.shortcuts import render
from .models import Interview

# Create your views here.
def board(request):
    interviews = Interview.objects.order_by('-id')
    return render(request,"interview.html", {'interviews':interviews})