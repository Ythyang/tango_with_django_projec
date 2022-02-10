from django.shortcuts import render

from django.http import HttpResponse
app_name= 'app1'
def about(request):
    return HttpResponse("Rango1 says hey there partner!")
    

# Create your views here.
