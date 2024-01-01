from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is first stage of development!")

def skill(request):
    return render(request, "constructor/index.html")
