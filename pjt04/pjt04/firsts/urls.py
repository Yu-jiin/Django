from django.urls import path
from . import views

# app_name = 'firsts'
urlpatterns = [
    path('', views.index, name='index'),
]
