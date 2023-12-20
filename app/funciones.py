from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator

#AQUÍ CREAREMOS DIFERENTES FUNCIONES QUE NOS VALIDEN CIERTOS ATRIBUTOS DE LOS MODELOS

#VALIDAR LONGITUD DEL RUT Y EL DÍGITO VERIFICADOR

# funciones.py

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "").upper()  # Eliminar puntos y guiones y convertir a mayúsculas
    if len(rut) != 9:
        return False  # El RUT debe tener 9 caracteres después de eliminar puntos y guiones
    try:
        int(rut[:-1])  # Verificar que los primeros 8 caracteres sean dígitos
    except ValueError:
        return False
    verificador = rut[-1]
    suma = 0
    multiplicador = 2
    for i in range(7, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    resultado = 11 - (suma % 11)
    if resultado == 11:
        resultado = 0
    if resultado == int(verificador):
        return True
    else:
        return False



def plural_a_singular(plural):
    plural_singular = {
        'Funcionarios': 'Funcionario',
        'Administradores': 'Administrador',
        'Coordinadores': 'Coordinador',
        'Psicopedagógos': 'Psicopedagógo',
        'Psicólogos': 'Psicólogo',
        'Terapeutas Ocupacionales': 'Terapeuta Ocupacional',
        'Fonoaudiologos': 'Fonoaudiologo',
        'Técnicos Diferenciales': 'Técnico Diferencial',
        'Técnicos Parvularios': 'Técnico Parvulario',   
    }
    return plural_singular.get(plural, plural)


# funcion para llamar a los grupos de un usuario

def get_user_group_name(user):
    # Inicializamos el nombre del grupo en el contexto con un valor predeterminado de None
    context = {
        'group_name': None,
    }

    # Verificamos si el usuario está autenticado
    if user.is_authenticated:
        # Buscamos el primer grupo al que pertenece el usuario
        group = Group.objects.filter(user=user).first()

        # Si encontramos un grupo, actualizamos el contexto con información sobre el grupo
        if group:
            # Obtenemos el nombre del grupo y su versión en singular
            group_name = group.name
            group_name_singular = plural_a_singular(group_name)

            # Actualizamos el contexto con la información del grupo
            context = {
                'group_name': group_name,
                'group_name_singular': group_name_singular,  
            }

    # Devolvemos el nombre del grupo en singular (o None si el usuario no está autenticado o no tiene grupo)
    return group_name_singular


# --------------------------------------------------------------------------------------------
























