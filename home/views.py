from django.shortcuts import render, redirect

def inicio(request):
    return render(request, 'home/index.html')

def acercademi(request):
    return render(request, 'home/about.html')

def contacto(request):
    return render(request, 'home/contacto.html')

def tratamiento(request):
    return render(request, 'home/tratamientos.html')

def tratamiento_endodoncia(request):
    return render(request, 'home/endodoncia.html')