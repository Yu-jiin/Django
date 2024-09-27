from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create2/', views.create2, name= 'create2'),
]
