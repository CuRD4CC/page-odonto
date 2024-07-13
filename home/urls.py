from django.urls import path
from home import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acercademi/', views.acercademi, name='acercademi'),
    path('contactanos/', views.contacto, name='contactanos'),
    path('tratamientos/', views.tratamiento, name='tratamientos'),
    path('tratamientos/endodoncia/', views.tratamiento_endodoncia, name='endodoncia'),
]