#AQUI CREAREMOS DIFERENTES FUNCIONES QUE NOS VALIDEN CIERTOS ATRIBUTOS DE LOS MODELOS

#VALIDAR LONGITUD DEL RUT Y EL DIGITO VERIFICADOR

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
