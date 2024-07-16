from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tratamiento

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

def tratamiento_cirugia(request):
    return render(request, 'home/cirugia_oral.html')

def tratamiento_estetica(request):
    return render(request, 'home/estetica_dental.html')

def tratamiento_higiene(request):
    return render(request, 'home/higiene_bucodental.html')

def tratamiento_implantologia(request):
    return render(request, 'home/implantologia.html')

def tratamiento_odontologia(request):
    return render(request, 'home/odontologia_general.html')

def tratamiento_odontopediatria(request):
    return render(request, 'home/odontopediatria.html')

def tratamiento_ortodoncia(request):
    return render(request, 'home/ortodoncia.html')

def tratamiento_periodoncia(request):
    return render(request, 'home/periodoncia.html')


# buscador
def buscar_tratamientos(request):
    query = request.GET.get('q', '').lower()
    if 'ortodoncia'.startswith(query):
        return redirect(reverse('ortodoncia'))
    elif 'cirugia oral'.startswith(query):
        return redirect(reverse('cirugia'))
    elif 'endodoncia'.startswith(query):
        return redirect(reverse('endodoncia'))
    elif 'estetica dental'.startswith(query):
        return redirect(reverse('estetica_dental'))
    elif 'higiene bucodental'.startswith(query):
        return redirect(reverse('higiene_bucodental'))
    elif 'implantologia'.startswith(query):
        return redirect(reverse('implantologia'))
    elif 'odontologia general'.startswith(query):
        return redirect(reverse('odontologia_general'))
    elif 'odontopediatria'.startswith(query):
        return redirect(reverse('odontopediatria'))
    elif 'periodoncia'.startswith(query):
        return redirect(reverse('periodoncia'))

    return render(request, 'home/resultados_busqueda.html', {'query': query})


