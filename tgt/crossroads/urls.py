from django.urls import path
from . import views


urlpatterns = [
    path('', views.crossroads, name='crossroads')
]
