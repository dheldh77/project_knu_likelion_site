from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def history(request):
    return render(request, 'history.html')

def five(request):
    return render(request, 'five.html')

def six(request):
    return render(request, 'six.html')

def seven(request):
    return render(request, 'seven.html')

def schedule(request):
    return render(request, 'schedule.html')

def about(request):
    return render(request, 'about.html')