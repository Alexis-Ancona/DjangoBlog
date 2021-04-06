from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Post, Categoria

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    paginator = Paginator(posts,2)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    ctx = {"posts": posts}
    return render(request, 'index.html', ctx)

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    ctx = {"detalle_post":post}
    return render(request, "post.html", ctx)

# __iexact hace que de igual si es mayuscula o minuscula
def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = "General"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "general")
        ).distinct()
    paginator = Paginator(posts,1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    ctx = {"posts": posts}
    return render(request, 'generales.html', ctx)

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = "Programacion"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "programacion")
        ).distinct()
    paginator = Paginator(posts,1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    ctx = {"posts": posts}
    return render(request, 'programacion.html', ctx)

def tutoriales(request):
    queryset = request.GET.get("bsucar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = "Tutoriales"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "tutoriales")
        ).distinct()
    paginator = Paginator(posts,1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    ctx = {"posts": posts}
    return render(request, 'tutoriales.html', ctx)

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = "Tecnologia"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "tecnologia")
        ).distinct()
    paginator = Paginator(posts,1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    ctx = {"posts": posts}
    return render(request, 'tecnologia.html', ctx)

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = "Videojuegos"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "videojuegos")
        ).distinct()
    paginator = Paginator(posts,1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    ctx = {"posts": posts}
    return render(request, 'videojuegos.html', ctx)
