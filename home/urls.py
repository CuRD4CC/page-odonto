from django.urls import path
from home import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acercademi/', views.acercademi, name='acercademi'),
    path('contactanos/', views.contacto, name='contactanos'),
    path('tratamientos/', views.tratamiento, name='tratamientos'),
    path('tratamientos/endodoncia/', views.tratamiento_endodoncia, name='endodoncia'),
    path('tratamientos/cirugia/', views.tratamiento_cirugia, name='cirugia'),
    path('tratamientos/estetica/', views.tratamiento_estetica, name='estetica'),
    path('tratamientos/higiene/', views.tratamiento_higiene, name='higiene'),
    path('tratamientos/implantologia/', views.tratamiento_implantologia, name='implantologia'),
    path('tratamientos/odontologia/', views.tratamiento_odontologia, name='odontologia'),
    path('tratamientos/odontopediatria/', views.tratamiento_odontopediatria, name='odontopediatria'),
    path('tratamientos/ortodoncia/', views.tratamiento_ortodoncia, name='ortodoncia'),
    path('tratamientos/periodoncia/', views.tratamiento_periodoncia, name='periodoncia'),
]