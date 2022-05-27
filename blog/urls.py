from urllib import request
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name= 'blog'),
    path('search/', views.search, name='search'),
    path('read/<slug:slug>/', views.postRead, name='read'),
    path('categoria/<slug:slug>/', views.category, name='category'),
]
