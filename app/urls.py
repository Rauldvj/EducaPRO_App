from django.urls import path
from . import views  # Importa tus vistas desde tu aplicación
from django.contrib.auth.decorators import login_required
from .views import profile_password_change, profile, home,  estudiante, anamnesis, bitacora, add_user, error

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista index
    # path("registro/", login_required(registro), name="registro"),  # Ruta para la vista registro
    path('accounts/login/', views.loginUser, name='login'),  # Ruta para la vista login
    path("home/", login_required(home), name="home"), #Ruta para la vista home
    path('perfil/', login_required(profile), name='perfil'),
    path('estudiante/', login_required(estudiante), name='estudiante'), #Ruta para la vista Estudiante
    path('bitacora/', login_required(bitacora), name='bitacora'),
    path('anamnesis/', login_required(anamnesis), name='anamnesis'),

    #CAMBIO DE CONTRASEÑA
     path('profile_password_change/', login_required(profile_password_change), name='profile_password_change'),

     #AGREGAR NUEVO USUARIO CREADO POR EL COORDINADOR:
     path('add_user/', login_required(add_user), name='add_user'),

     #PAGINA DE ERROR:
     path('error/', login_required(error), name='error'),

     #URL CUSTOM LOGIN
     path('custom_login/', views.custom_login, name='custom_login'),
]