from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/cities/<int:region_id>/', views.get_cities, name='get_cities'),
    path('', views.home, name='home'),
    path('murojaat', views.murojaat, name='murojaat'),
    path('persons/<int:cat_id>/', views.persons, name='persons'),
    path('api/leaders/<int:region_id>/', views.get_leaders, name='get_leaders'),
    path('api/city_leader/<int:city_id>/', views.get_city_leader, name='get_city_leader'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('vote/', views.vote, name='vote'),
]