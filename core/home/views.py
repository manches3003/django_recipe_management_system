from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"index.html")

def success(request):
    return HttpResponse("<h1> hey...i m from the success tag </h1>")