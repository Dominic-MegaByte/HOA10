from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about_me'),
    path('know/', views.know, name='know_me_well'),
    path('signs/', views.signs, name='zodiac_signs'),
]