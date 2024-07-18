from django.urls import path
from . import views
from .views import CrearExperiencia, EditarExperiencia, EliminarExperiencia
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.mi_experiencia, name='experiencias'),
    path('resenia/', views.tu_resenia, name='resenia'),
    path('experiencias/crear/', CrearExperiencia.as_view(), name='crear'),
    path('experiencias/editar/<int:pk>/', EditarExperiencia.as_view(), name='editar'),
    path('experiencias/eliminar/<int:pk>/', EliminarExperiencia.as_view(), name='eliminar'),
]


