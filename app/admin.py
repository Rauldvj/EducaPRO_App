from django.contrib import admin
from .models import Curso, Estudiante, ApoderadoTitular, Bitacora, NivelAcademico, \
    Asistencia, RegistroPie, ApoderadoSuplente1, ApoderadoSuplente2

#Register your models here.

#____________________________________________________________________________________________________________

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nivel', 'curso', 'letra_curso']
    search_fields = ['curso']
    list_filter = ('nivel', 'curso')
admin.site.register(Curso, CursoAdmin)

#____________________________________________________________________________________________________________
class RegistroPieAdmin(admin.ModelAdmin):
    list_display = ['curso', 'estudiante', 'apoderado', 'ApoderadoSuplente1', 'ApoderadoSuplente2', 'enable']
    search_fields = ['estudiante']
    list_filter = ['curso', 'estudiante']
admin.site.register(RegistroPie, RegistroPieAdmin)



#____________________________________________________________________________________________________________

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombres', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento',\
    'direccion', 'telefono', 'correo', 'region', 'comuna', 'etnia', 'comorbilidad']
    search_fields = ['rut', 'apellido_paterno']
    list_filter = ('rut', 'apellido_paterno')
admin.site.register(Estudiante, EstudianteAdmin)
#____________________________________________________________________________________________________________

class ApoderadoTitularAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombres', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento',\
    'direccion', 'telefono', 'correo', 'region', 'comuna', 'etnia', 'salud', 'renta']
    search_fields = ['rut', 'apellido_paterno']
    list_filter = ('rut', 'apellido_paterno')
admin.site.register(ApoderadoTitular, ApoderadoTitularAdmin)

#____________________________________________________________________________________________________________
class ApoderadoSuplente1Admin(admin.ModelAdmin):
    list_display = ['rut', 'nombres', 'apellido_paterno', 'apellido_materno',\
    'direccion', 'telefono', 'region', 'comuna']
    search_fields = ['rut', 'apellido_paterno']
    list_filter = ('rut', 'apellido_paterno')
admin.site.register(ApoderadoSuplente1, ApoderadoSuplente1Admin)

#____________________________________________________________________________________________________________
class ApoderadoSuplente2Admin(admin.ModelAdmin):
    list_display = ['rut', 'nombres', 'apellido_paterno', 'apellido_materno',\
    'direccion', 'telefono', 'region', 'comuna']
    search_fields = ['rut', 'apellido_paterno']
    list_filter = ('rut', 'apellido_paterno')
admin.site.register(ApoderadoSuplente2, ApoderadoSuplente2Admin)


#____________________________________________________________________________________________________________

# Definición de la clase AsistenciaAdmin para el panel de administración
class AsistenciaAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Filtramos las opciones del campo de selección del curso en el panel de administración
        if db_field.name == "curso":
            # Reemplaza "1" con el ID del curso específico al que deseas restringir las opciones
            kwargs["queryset"] = Curso.objects.filter(id=1)  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    list_display = ['curso', 'estudiante', 'fecha', 'presente']
    search_fields = ['estudiante']
    list_filter = ['curso', 'estudiante']

# Registro del modelo Asistencia en el panel de administración
admin.site.register(Asistencia, AsistenciaAdmin)



#_____________________________________________________________________________________________________________

class BitacoraAdmin(admin.ModelAdmin): 
    list_display = ['fecha', 'hora_entrada', 'hora_salida', 'estudiante']
    search_fields = ['estudiante']
admin.site.register(Bitacora, BitacoraAdmin)

#AQUI REGISTRAMOS NUESTROS MODELOS Y MODELOS DE ADMIN


admin.site.register(NivelAcademico)


