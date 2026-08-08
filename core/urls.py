from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact')
]