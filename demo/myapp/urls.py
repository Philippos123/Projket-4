from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('todos/', views.todos, name="todos"),
    path('booking/', views.book, name="book"),
    path('contact/', views.contact, name="contact"),
    
]