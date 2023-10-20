from django.contrib import admin
from .models import Profile, Region, Comuna

admin.site.register(Region)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ['region', 'comuna']
    search_fields = ['comuna']
admin.site.register(Comuna, ComunaAdmin)
#---------------------------------------------------------------------
# PROFILE DETALLADO
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno', 'direccion', 'region', 'comuna','telefono', 'grado', 'user_group')
    search_fields =('rut', 'user__username', 'user__groups__name')
    list_filter = ('user__groups', 'rut', 'apellido_paterno')

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

admin.site.register(Profile, ProfileAdmin)