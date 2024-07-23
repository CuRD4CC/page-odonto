from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.mi_experiencia, name='experiencias'),
    path('resenia/', views.tu_resenia, name='resenia'),
    path('crear-experiencia/', views.crear_experiencia, name='crear_experiencia'),
    path('aniadir-experiencia/', views.aniadir_blog, name='aniadir_blog'),
    
]