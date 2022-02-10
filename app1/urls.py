from .views import about
from django.urls import path
app_name= 'app1'
urlpatterns = [
    path('', about),

]