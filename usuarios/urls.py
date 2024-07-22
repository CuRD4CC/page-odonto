from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/login.html'), name='logout'),
    path('usuarios/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.VerPerfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', views.CambiarPassword.as_view(), name='cambiar_pass'),
]
