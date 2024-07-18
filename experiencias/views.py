from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout

# def mi_experiencia(request):
#     return render(request, 'experiencias/mi_experiencia.html')

def editar_experiencia(request):
    return render(request, 'experiencias/editar_experiencia.html')

def eliminar_experiencia(request):
    return render(request, 'experiencias/eliminar_experiencia.html')

def crear_experiencia(request):
    return render(request, 'experiencias/crear_experiencia.html')

def tu_resenia(request):
    return render(request, 'experiencias/post.html')


#### modificando el blog ###
def mi_experiencia(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'experiencias/mi_experiencia.html', context)

def aniadir_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/add-blog/')
    except Exception as e:
        print(e)

    return render(request, 'experiencias/crear_experiencias.html', context)