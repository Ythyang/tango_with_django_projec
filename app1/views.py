from django.shortcuts import render

from django.http import HttpResponse
app_name= 'app1'
def about(request):
    
    return render(request, 'about.html')
