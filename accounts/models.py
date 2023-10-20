from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .opcionesAcc import opciones_grado

#____________________________________________________________________________________________________________
#MODELO REGION 

class Region(models.Model):
    region = models.CharField(max_length=100, verbose_name='Region')
    
    def __str__(self):
        return self.region
        
#____________________________________________________________________________________________________________

#MODELO COMUNA QUE HEREDA LA REGION DEL MODELO "REGION"
class Comuna(models.Model):
    comuna = models.CharField(max_length=100, verbose_name='Comuna')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.comuna}'
        
#____________________________________________________________________________________________________________

# PERFIL DE USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    rut = models.CharField(max_length=15, verbose_name='Rut')
    nombres = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, null=True, blank=True, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Region')
    comuna = models.ForeignKey(Comuna, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Comuna')
    telefono = models.CharField(max_length=9, null=True, blank=True, verbose_name='Teléfono')
    grado = models.CharField(max_length=100, choices=opciones_grado, verbose_name='Grado Académico')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        default_region = Region.objects.first()  # Obtener la primera región por defecto
        default_comuna = Comuna.objects.first()
        Profile.objects.create(user=instance, region=default_region, comuna=default_comuna)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)