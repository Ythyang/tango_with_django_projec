from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("<a href='/rango/about/'>About</a>")

# Create your views here.