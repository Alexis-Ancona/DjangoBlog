from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
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
        )
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
        )
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
        )
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
        )
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
        )
    ctx = {"posts": posts}
    return render(request, 'videojuegos.html', ctx)
