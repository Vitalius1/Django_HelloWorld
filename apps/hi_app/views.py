from django.shortcuts import render

def index(request):
    print ("hello world")
    return render(request, "hi_app/index.html")

# Create your views here.
