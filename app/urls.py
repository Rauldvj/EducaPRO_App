from django.urls import path
from . import views  # Importa tus vistas desde tu aplicación

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista index
    path('accounts/login/', views.login, name='login'),  # Ruta para la vista login
    path('estudiante/', views.estudiante, name='estudiante'), #Ruta para la vista Estudiante
    path('bitacora/', views.Bitacora, name='bitacora')
]