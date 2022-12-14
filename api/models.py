from django.db import models
#from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Cliente(models.Model):
    documento = models.CharField(max_length=20, null=True)
    tipo_documento = models.CharField(max_length=20, null=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Cliente")
    genero = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    acceptance_tm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Tipo_tramite (models.Model):    
    descripcion_tipo = models.CharField(max_length=200,null=True,blank=True)
    nombre_tipo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

class Persona(models.Model):
    documento = models.IntegerField()
    tipo_documento = models.CharField(max_length=20, null=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Persona")
    genero = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    acceptance_tm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class CIIU(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200, null=True)
    estado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)    
    update_at = models.DateTimeField(auto_now=True, null=True)

class Tributos(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

class Responsabilidad_Fiscal(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

class Estado_Servicio(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

class Servicio(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

class Gestion_Servicio(models.Model):
    observacion = models.CharField(max_length=1000, null=True)
    id_servicio = models.IntegerField()
    id_estado_servicio = models.IntegerField()
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Detalle_Servicio(models.Model):
    id_cliente = models.IntegerField()
    id_servicio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)