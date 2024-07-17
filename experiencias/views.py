from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Experiencia
from .forms import ExperienciaForm

def mi_experiencia(request):
    return render(request, 'experiencias/mi_experiencia.html')

def editar_experiencia(request):
    return render(request, 'experiencias/editar_experiencia.html')

def eliminar_experiencia(request):
    return render(request, 'experiencias/eliminar_experiencia.html')

def crear_experiencia(request):
    return render(request, 'home/crear_experiencia.html')

def tu_resenia(request):
    return render(request, 'experiencias/post.html')



class CrearExperiencia(LoginRequiredMixin, CreateView):
    model = Experiencia
    form_class = ExperienciaForm
    template_name = 'usuarios/crear_experiencia.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EditarExperiencia(LoginRequiredMixin, UpdateView):
    model = Experiencia
    form_class = ExperienciaForm
    template_name = 'usuarios/editar_experiencia.html'

class EliminarExperiencia(LoginRequiredMixin, DeleteView):
    model = Experiencia
    template_name = 'usuarios/eliminar_experiencia.html'
    success_url = '/experiencias/'
