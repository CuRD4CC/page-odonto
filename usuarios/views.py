from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import NuestroFormularioRegistro

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



# def registro(request):
    
#     formulario = NuestroFormularioRegistro
    
#     if request.method == "POST":
#         formulario = NuestroFormularioRegistro(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('login')
#     return render(request, 'usuarios/registro.html', {'formulaio': formulario})