# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),

    path('create/skill/', views.skill, name='index'),
]
