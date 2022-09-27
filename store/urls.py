
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('home_view', views.home_view,name='home-view'),
    path('dorcas', views.dorcas,name='dorcas'),
   
]