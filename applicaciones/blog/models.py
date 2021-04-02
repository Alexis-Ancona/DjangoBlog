from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoría', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoría Activada/Categoría no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres de Autor', max_length = 255, null = False, blank = False)
    apellidos = models.CharField('Apellidos de Autor', max_length = 255, null = False, blank = False)
    facebook = models.URLField('Facebook', blank = True, null = True)
    twitter = models.URLField('Twitter', blank = True, null = True)
    instagram = models.URLField('Instagram', blank = True, null = True)
    web = models.URLField('Web', blank = True, null = True)
    email = models.EmailField('Correo Electrónico', blank = False, null = False)
    estado = models.BooleanField('Autor Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'{self.apellidos}, {self.nombres}'
