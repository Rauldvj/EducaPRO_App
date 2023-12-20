from typing import Any

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from django.contrib import messages #Importamos mensajes
from .mixins import AdminCoordinatorRequiredMixin
from .funciones import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from .funciones import get_user_group_name, plural_a_singular
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash #Importamos para el cambio de contraseña
from .forms import * #Importamos los modelos de formularios para realizar la vista
from django.core.paginator import Paginator 
from django.http import Http404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .models import Profile



# ------------------------------------------------------------------------------------------------------------------
#PAGINA DE ERROR
def error(request):
    return render(request, 'error.html')



# """ Crea vista del index """
def index(request):
    
    return render(request, "index.html")
#  -----------------------------------------------------------------   

#Vista para Crear un Nuevo Usuario

# def registro(request):
#     data = {
#         "form": RegistroUsuarioForm()
#     }
#     if request.method == "POST":
#         formulario = RegistroUsuarioForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
#             login(request, user)
#             messages.success(request, "¡Usuario Creado Correctamente!")
#             return redirect(to="perfil")     
#         data["form"] = formulario
#     return render(request, "registration/registro.html", data)


#  -----------------------------------------------------------------   
# Crea vista para el login

def loginUser(request):
    return render(request, 'registration/login.html')
#  -----------------------------------------------------------------  
#Crea vista para el Home

def home(request):
    # Obtener el nombre del grupo para el usuario actual
    group_name_singular = get_user_group_name(request.user)

    # Pasamos group_name al contexto si lo necesitas en tu template
    context = {'group_name_singular': group_name_singular}

    return render(request, 'home.html', context)
        


#  -----------------------------------------------------------------  
#Crea vista para registro de Estudiante

def estudiante(request):
    
    data = {
        'form': EstudianteForm()
    }
    if request.method == 'POST':
        formulario = EstudianteForm(data=request.POST) #Recibimos la data del formulario de Estudiante
        if formulario.is_valid(): #Si el formulario es valido
            formulario.save() #Se registran los datos en la BD
            data['mensaje'] = 'Estudiante registrado' #Mensaje de éxito
        
        else:
            data['form'] = formulario #Si el formulario posee errores, este no se guardara
    return render(request, 'registro/estudiante.html', data)
    

def anamnesis(request):
    data = {
        'form': AnamnesisForm()
    }
    if request.method == 'POST':
        formulario = AnamnesisForm(data=request.POST) #Recibimos la data del formulario de Anamnesis
        if formulario.is_valid(): #Si el formulario es valido
            formulario.save() #Se registran los datos en la BD
            data['mensaje'] = 'Anamnesis registrado' #Tail de éxito
        
        else:
            data['form'] = formulario #Si el formulario posee errores, este no se guardara
    return render(request, 'informes/anamnesis.html', data)
        


   # VISTAS SOLO PARA LOS DIFERENTES INFORMES

def bitacora(request):
    return render(request, 'informes/bitacora.html') 




#  -----------------------------------------------------------------  
#Crea vista para el Perfil
def profile(request):
    # Obtener el usuario y el perfil asociado
    user = request.user
    profile = user.profile

    # Obtener el nombre del grupo para el usuario actual
    group_name_singular = get_user_group_name(user)

    if request.method == 'POST':
        # Procesar el formulario si la solicitud es POST
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            # Guardar los cambios en el usuario y el perfil si ambos formularios son válidos
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('perfil')
        else:
            # Mostrar mensajes de error si hay problemas con los formularios
            messages.error(request, 'Error al actualizar el perfil. Verifica los errores en el formulario.')
    else:
        # Si la solicitud no es POST, inicializar los formularios con los datos actuales
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    # Obtener todos los usuarios, grupos y perfiles para mostrar en el contexto
    all_users = User.objects.all()
    all_groups = Group.objects.all()
    user_profiles = []

    for user in all_users:
        profile = user.profile
        user_groups = user.groups.all()
        #Esta variable es para el singular de los grupos
        processed_group = [plural_a_singular(group.name) for group in user_groups]

        # Agregar información de cada usuario al listado
        user_profiles.append({
            'user': user,
            'groups': processed_group,
            'profile': profile
        })

    # Crear el contexto con la información recolectada
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'group_name_singular': group_name_singular,
        'user_profiles': user_profiles,
        'all_groups': all_groups,
    }

    # Renderizar la plantilla con el contexto
    return render(request, 'perfiles/perfil.html', context)


#CAMBIAR CONTRASEÑA AL USUARIO
def profile_password_change(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user

        if user.check_password(old_password):
            if new_password1 == new_password2:
                # Cambio de contraseña y guardado en la base de datos
                user.set_password(new_password1)
                user.save()

                # Actualizar el campo creado_por_coordinador en el modelo Profile
                try:
                    profile = Profile.objects.get(user=user)
                    profile.creado_por_coordinador = False
                    profile.save()
                except Profile.DoesNotExist:
                    # Maneja el caso si el perfil no existe
                    pass

                # Actualización de la sesión para evitar cerrar la sesión después de cambiar la contraseña
                update_session_auth_hash(request, user)

                # Mensaje de éxito y redirección a la página de perfil
                messages.success(request, 'Contraseña cambiada exitosamente.')
                return redirect('perfil')
            else:
                messages.error(request, 'Las nuevas contraseñas no coinciden.')
        else:
            messages.error(request, 'La contraseña actual es incorrecta.')

    return render(request, 'perfiles/profile_password_change.html')



#FUNCION PARA CREAR UN USUARIO DESDE EL FORMULARIO SI ES UN ADMINISTRADOR O COORDINADOR
# Decorador para requerir login y verificar si es "Administrador" o "Coordinador"

@user_passes_test(lambda u: u.is_authenticated and (u.is_superuser or u.groups.filter(name__in=['Coordinadores', 'Administradores']).exists()))

def add_user(request):
    group_name_singular = get_user_group_name(request.user)

    # Pasamos group_name al contexto si lo necesitas en tu template
   

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Obtener los grupos
            group_id = request.POST.get('group')
            group = Group.objects.get(id=group_id)

            # Crear un usuario sin guardarlo aún en la base de datos
            user = form.save(commit=False)

            # Asignar una contraseña por defecto al nuevo usuario
            # Y después se podrá cambiar
            user.set_password('contraseña')
            
            # Convertir al usuario a staff solo si el grupo es '2' o '3'
            if group_id in ['2', '3']:
                user.is_staff = True

            # Guardar el usuario en la base de datos
            user.save()

            # Cambiar el grupo asignado por defecto
            user.groups.clear()
            # Asignar el grupo al usuario
            user.groups.add(group)

            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('perfil') 
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrija los errores.')

    else:
        form = UserCreationForm()
    

    # Obtener todos los grupos desde la base de datos
    groups = Group.objects.all()
    

    # Crear una lista que contiene los nombres de los grupos convertidos a singular y en mayúsculas
    singular_groups = [plural_a_singular(group.name).capitalize() for group in groups]

    # Crear un diccionario de contexto con la variable 'groups' que es una lista de tuplas
    # que vinculan los objetos Group con los nombres de grupos singulares
    context = {
        'form': form,
        'groups': zip(groups, singular_groups),
        'group_name_singular': group_name_singular
    }

    # Renderizar la plantilla 'add_user.html' con el contexto
    return render(request, 'perfiles/add_user.html', context)

#CREAMOS UN LOGIN PERSONALIZADO
def custom_login(request, *args, **kwargs):
    # Utilizamos la vista de login de Django
    response = LoginView.as_view()(request, *args, **kwargs)

    # Si el formulario es válido
    if request.method == 'POST' and response.status_code == 302:
        # Acceder al Perfil del Usuario
        profile = request.user.profile if request.user.is_authenticated else None

        # Verificamos si el Usuario fue creado por el "Coordinador"
        if profile and profile.creado_por_coordinador:
            messages.warning(request, 'Debe cambiar la contraseña por defecto ahora')

            # Redirigimos al Perfil de usuario para que cambie su contraseña
            return redirect(reverse_lazy('profile_password_change'))

    return response