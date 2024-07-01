from django.urls import path
from home import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acercademi', views.acercademi, name='acercademi'),
    # path('profesor/', views.profesor, name='profesor'),
    # path('alumno/', views.alumno, name='alumno'),
    # path('especializaciones/', views.especializacion, name='especializacion'),
    # path('cursos/', views.curso, name='curso'),
    # path('buscar/', views.buscar, name='buscar'),
]