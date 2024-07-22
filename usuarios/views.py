from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import NuestroFormularioRegistro, EditarPerfil, CambiarPassword as NuestroFormularioCambiarPassword
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.forms import DatosExtraForm
from usuarios.models import DatosExtra

def user_login(request):
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
    
            
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                django_login(request, user)
                DatosExtra.objects.get_or_create(user=user)
                return redirect('inicio')
            else:
                formulario.add_error(None, 'Usuario o contraseña incorrectos.')
            
    return render(request, 'usuarios/login.html', {'formulario': formulario})
            
def registro(request):
    if request.method == 'POST':
        formulario = NuestroFormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('inicio')
            else:
                print(formulario.errors)  # Imprimir los errores del formulario
    else:
        formulario = NuestroFormularioRegistro()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, initial={'avatar': request.user.datosextra.avatar}, instance=request.user)
        formulario_datos_extra = DatosExtraForm(request.POST, request.FILES, instance=request.user.datosextra)
        if formulario.is_valid():
            formulario.save()
            formulario_datos_extra.save()
            return redirect('editar_perfil')
    else:
        formulario = EditarPerfil(instance=request.user)
        formulario_datos_extra = DatosExtraForm(instance=request.user.datosextra)
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario, 'formulario_datos_extra': formulario_datos_extra})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    form_class = NuestroFormularioCambiarPassword
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('editar_perfil')

def VerPerfil(request):
    return render(request, 'usuarios/ver_perfil.html')