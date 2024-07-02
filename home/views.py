from django.shortcuts import render, redirect

def inicio(request):
    return render(request, 'home/index.html')

def acercademi(request):
    return render(request, 'home/about.html')

def contacto(request):
    return render(request, 'home/contacto.html')