from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import Region, Comuna
from .funciones import validar_rut
from django.core.validators import EmailValidator
from .opciones import opciones_ascendencia, opcion_letra_curso, opciones_aprendizaje ,opcionesApoyo, opcionesBloque, opciones_salud


#AQUÍ CREAREMOS LOS MODELOS PARA NUESTRA APLICACIÓN

#MODELO QUE CREA NIVEL ACADÉMICO DEL CURSO  

class NivelAcademico(models.Model):
    nivel = models.CharField(max_length=100, verbose_name='Nivel Academico')
    def __str__(self):
        return self.nivel
    
    class Meta:
        verbose_name = 'Nivel Academico'
        verbose_name_plural = 'Niveles Academicos'
#____________________________________________________________________________________________________________

#MODELO PARA CREAR UN CURSO

class Curso(models.Model):
    nivel = models.ForeignKey(NivelAcademico, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100, verbose_name='Curso')
    letra_curso = models.CharField(max_length=1, choices=opcion_letra_curso, verbose_name='Letra')
    def __str__(self):
        return f'{self.curso} {self.letra_curso}'

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
#____________________________________________________________________________________________________________
#MODELO PARA CREAR UN ESTUDIANTE

class Estudiante(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name='Rut') 
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    correo = models.EmailField(validators=[EmailValidator()], verbose_name='Correo Electrónico')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region' )
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name='Comuna')
    etnia = models.CharField(max_length=100, default='No Posee', choices=opciones_ascendencia, verbose_name='Ascendencia')
    comorbilidad = models.TextField(verbose_name='Comorbilidad')
    
    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

# Definición de la señal pre_save para estandarizar el formato de las cadenas
@receiver(pre_save, sender=Estudiante)
def estudiante_pre_save(sender, instance, *args, **kwargs):
    instance.nombres = instance.nombres.title()
    instance.apellido_paterno = instance.apellido_paterno.title()
    instance.apellido_materno = instance.apellido_materno.title()
    instance.direccion = instance.direccion.title()  # Asegura la primera letra en mayúscula en cada palabra de la dirección
    # Asegura que la comorbilidad esté en minúsculas
    instance.comorbilidad = instance.comorbilidad.lower()
#____________________________________________________________________________________________________________

#____________________________________________________________________________________________________________
#MODELO PARA CREAR UN APODERADO TITULAR

class ApoderadoTitular(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name='Rut') 
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    correo = models.EmailField(validators=[EmailValidator()], verbose_name='Correo Electrónico')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region' )
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name='Comuna')
    etnia = models.CharField(max_length=100, default='No Posee', choices=opciones_ascendencia, verbose_name='Ascendencia')
    salud = models.CharField(max_length=100, default='Seleccione', choices=opciones_salud, verbose_name='Salud')
    renta = models.PositiveIntegerField(verbose_name='Renta')
    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'

    class Meta:
        verbose_name = 'Apoderado Titular'
        verbose_name_plural = 'Apoderados Titulares'
#____________________________________________________________________________________________________________
#MODELO PARA REGISTRAR UN APODERADO SUPLENTE 1

class ApoderadoSuplente1(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name='Rut') 
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region' )
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name='Comuna')
    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'
    
    class Meta:
        verbose_name = 'Apoderado Suplente 1'
        verbose_name_plural = 'Apoderados Suplentes 1'


#____________________________________________________________________________________________________________
#____________________________________________________________________________________________________________
#MODELO PARA REGISTRAR UN APODERADO SUPLENTE 2

class ApoderadoSuplente2(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name='Rut') 
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region' )
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name='Comuna')
    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'
    

    class Meta:
        verbose_name = 'Apoderado Suplente 2'
        verbose_name_plural = 'Apoderados Suplentes 2'

#____________________________________________________________________________________________________________


#MODELO PARA UNA Registro en el PIE

class RegistroPie(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
    apoderado = models.ForeignKey(ApoderadoTitular, on_delete=models.CASCADE, verbose_name='Apoderado')
    ApoderadoSuplente1 = models.ForeignKey(ApoderadoSuplente1, on_delete=models.CASCADE, verbose_name='Apoderado Suplente 1')
    ApoderadoSuplente2 = models.ForeignKey(ApoderadoSuplente2, on_delete=models.CASCADE, verbose_name='Apoderado Suplente 2')
    enable = models.BooleanField(default=True, null=True, verbose_name='Alumno Regular')
    def __str__(self):
        return f'{self.curso} {self.estudiante}'
    
    class Meta: 
        verbose_name = 'Pie'
        verbose_name_plural = 'Pies'
#____________________________________________________________________________________________________________

# Definición del modelo Asistencia
class Asistencia(models.Model):
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        verbose_name='Curso',
        # Aquí limitamos las opciones del curso al que deseamos asignar
        # Asegúrate de reemplazar '1' con el ID correcto del curso específico
        limit_choices_to={'id': 1}  
    )
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha')
    presente = models.BooleanField(default=False, null=True, blank=True, verbose_name='Presente')

    def __str__(self):
        return f'Asistencia {self.id}'
    
    class Meta: 
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

#____________________________________________________________________________________________________________


#Modelo para Bitacora

class Bitacora(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    hora_entrada = models.TimeField(auto_now=True)
    hora_salida = models.TimeField(auto_now=True)
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
    
    bloque1 = models.CharField(max_length=20, choices=opcionesBloque,default='Primer bloque', verbose_name='Bloque')
    objetivoClase1 = models.CharField(max_length=350, verbose_name='Objetivo de la Clase')  
    objetivoPaci1 = models.CharField(max_length=350, verbose_name='Objetivo del Paci')
    desarrolloActividad1 = models.TextField(verbose_name='Desarrollo de la actividad')
    material1= models.TextField(verbose_name='Material utilizado')
    personaMaterial1 = models.CharField(max_length=100, verbose_name='Persona que entrega el material')
    reaccion1 = models.CharField(max_length=350, verbose_name='Reaccion del alumno frente a la actividad')
    estadoAprendizaje1 = models.CharField(max_length=20, default='Selecione', choices=opciones_aprendizaje, verbose_name='Estado aprendizaje')
    apoyoDocente1 = models.CharField(max_length=20, default='Seleccione', choices=opcionesApoyo, verbose_name='Apoyo del Docente durante la actividad')
    obervacionesGenerales1 = models.TextField(verbose_name='Observaciones generales')
    
    bloque2b = models.CharField(max_length=20, choices=opcionesBloque,default='Segundo bloque', verbose_name='Bloque')
    objetivoClase2b = models.CharField(max_length=350, verbose_name='Objetivo de la Clase')  
    objetivoPaci2b = models.CharField(max_length=350, verbose_name='Objetivo del Paci')
    desarrolloActividad2b = models.TextField(verbose_name='Desarrollo de la actividad')
    material2b = models.TextField(verbose_name='Material utilizado')
    personaMaterial2b = models.CharField(max_length=100, verbose_name='Persona que entrega el material')
    reaccion2b = models.CharField(max_length=350, verbose_name='Reaccion del alumno frente a la actividad')
    estadoAprendizaje2b = models.CharField(max_length=20, default='Selecione', choices=opciones_aprendizaje, verbose_name='Estado aprendizaje')
    apoyoDocente2b = models.CharField(max_length=20, default='Seleccione', choices=opcionesApoyo, verbose_name='Apoyo del Docente durante la actividad')
    obervacionesGenerales2b = models.TextField(verbose_name='Observaciones generales')
    
    def __str__(self):  
        return f'{self.fecha}, {self.hora_entrada}, {self.hora_salida} {self.estudiante}'
    
    class Meta: 
        verbose_name = 'Bitacora'
        verbose_name_plural = 'Bitacoras'
    