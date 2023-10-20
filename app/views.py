from django.shortcuts import render
from .forms import EstudianteForm #Importamos los modelos de formularios para realizar la vista

# Create your views here.

# """ Crea vista del index """

def index(request):
    return render(request, "index.html")

#  -----------------------------------------------------------------   
# Crea vista para el login

def login(request):
    return render(request, 'registration/login.html')
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
            data['mensaje'] = 'Estudiante registrado' #Mensaje de exito
        
        else:
            data['form'] = formulario #Si el formulacio posee errores, este no se guardara
    return render(request, 'registro/estudiante.html', data)
    
    
    
        
   # VISTAS SOLO PARA LOS DIFERENTES INFORMES
   
def Bitacora(request):
    return render(request, 'informes/bitacora.html') 