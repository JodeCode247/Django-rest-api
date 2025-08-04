from django.urls import re_path
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('book/<int:id>/',views.getBook),
    re_path('create_book/', views.createBook),
    path('UpdateBook/<int:id>/', views.UpdateBook),
    re_path('signup', views.signup),
    path('get_fruit/<int:id>/',views.getFruitInfo),
    path('filterFruits/',views.filterFruits),
    re_path('test_token', views.test_token),
]
