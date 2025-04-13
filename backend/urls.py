from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('person/<int:pk>/', views.person_detail, name='person_detail'),
    path('api/cities/<int:region_id>/', views.get_cities, name='get_cities'),
    path('', views.home, name='home'),
    path('murojaat', views.murojaat, name='murojaat'),
    path('purpose', views.purpose, name='purpose'),
    path('terms', views.terms, name='terms'),
    path('school', views.school, name='school'),
    path('recruitment', views.recruitment, name='recruitment'),
    path('egov', views.egov, name='egov'),
    path('open', views.open, name='open'),
    path('faqs', views.faqs, name='faqs'),
    path('ijro', views.ijro, name='ijro'),
    path('investment', views.investment, name='investment'),
    path('employees', views.employees, name='employees'),
    path('openness', views.openness, name='openness'),
    path('opendatadb', views.opendatadb, name='opendatadb'),
    path('corruption', views.corruption, name='corruption'),
    path('eservice', views.eservice, name='eservice'),
    path('persons/<int:cat_id>/', views.persons, name='persons'),
    path('newstypes/<int:cat_id>/', views.newstypes, name='newstypes'),
    path('filetypes/<int:cat_id>/', views.filetypes, name='filetypes'),
    path('api/leaders/<int:region_id>/', views.get_leaders, name='get_leaders'),
    path('api/city_leader/<int:city_id>/', views.get_city_leader, name='get_city_leader'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('vote/', views.vote, name='vote'),
    path('about/', views.about, name='about'),
]