from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subs'),
    path('getintouch/', views.getintouch, name='getintouch')
]