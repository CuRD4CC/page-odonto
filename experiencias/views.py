from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import BlogModel
from django.contrib.auth import logout


def editar_experiencia(request):
    return render(request, 'experiencias/editar_experiencia.html')

def eliminar_experiencia(request):
    return render(request, 'experiencias/eliminar_experiencia.html')

def crear_experiencia(request):
    form = BlogForm()
    return render(request, 'experiencias/crear_experiencia.html', {'form': form})

def tu_resenia(request):
    return render(request, 'experiencias/post.html')

def mi_experiencia(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'experiencias/mi_experiencia.html', context)

@login_required
def PostBlog(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'experiencias/post.html', context)

@login_required
def aniadir_blog(request):
    form = BlogForm()
    context = {'form': form}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
                image = request.FILES.get('image', '')

                blog_obj = BlogModel.objects.create(
                    user=user, title=title,
                    content=content, image=image
                )
                return redirect('experiencias')
            else:
                print('Form is not valid')
                print(form.errors)
    except Exception as e:
        print(f'Error: {e}')

    return render(request, 'experiencias/mi_experiencia.html', context)

