from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/cities/<int:region_id>/', views.get_cities, name='get_cities'),
    path('', views.home, name='home'),
    path('murojaat', views.murojaat, name='murojaat'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('vote/', views.vote, name='vote'),
]