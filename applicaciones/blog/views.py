from django.shortcuts import render
from .models import Post, Categoria
# Create your views here.

def home(request):
    posts = Post.objects.filter(estado = True)
    ctx = {"posts": posts}
    return render(request, 'index.html', ctx)

def generales(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = "General"))
    ctx = {"posts": posts}
    return render(request, 'generales.html', ctx)

def programacion(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = "Programacion"))
    ctx = {"posts": posts}
    return render(request, 'programacion.html', ctx)

def tutoriales(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = "Tutoriales"))
    ctx = {"posts": posts}
    return render(request, 'tutoriales.html', ctx)

def tecnologia(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = "Tecnologia"))
    ctx = {"posts": posts}
    return render(request, 'tecnologia.html', ctx)

def videojuegos(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = "Videojuegos"))
    ctx = {"posts": posts}
    return render(request, 'videojuegos.html', ctx)
