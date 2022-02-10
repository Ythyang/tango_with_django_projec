from .views import about
from . import views
from django.urls import path
app_name= 'app1'

urlpatterns = [
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('', about),
    

]