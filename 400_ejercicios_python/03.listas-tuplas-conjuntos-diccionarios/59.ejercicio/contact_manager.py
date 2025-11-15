"""
59)Diccionario de Contactos: Crea un diccionario de contactos con nombres y números de 
teléfono.
"""
def accent(text):
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"
    }
    resultado = ""

    for caracter in text: 
        # Si el caracter tiene una versión sin tilde, úsala.
        # Si no existe reemplazo, conserva el caracter original.
        caracter_sin_tilde = reemplazos.get(caracter, caracter)

        # Agregar el caracter procesado al resultado final
        resultado += caracter_sin_tilde
    
    return resultado

def detect_str(valor,dato):
    while not valor.strip().isalpha():
        print(f"⚠️ El {dato} solo debe contener letras.")
        valor=input(f"Ingrese el {dato} de la persona").strip()
    return valor

def detect_int(valor,dato):
    while not valor.isdigit():
        print(f"⚠️ El {dato} solo debe contener dígitos.")
        valor=input(f"Ingrese nuevamente el {dato} de la persona: ").strip()
    return int(valor)

def add_contact(dic,nombre,telefono): 
    """
    Agrega un contacto al diccionario.
    No imprime nada y no pide input().
    """
    nombre = nombre.strip()

    if not nombre: 
        return False, "El nombre está vacío"
    
    if not telefono.isdigit():
        return False, "El teléfono desde ser numérico"
    
    dic[nombre] = int(telefono)
    return True, f"Contacto agregado: {nombre} (+{telefono})"

def del_contact(dic, nombre):
    """
    Elimina un contacto por nombre exacto o parcialmente.
    """
    nombre = accent(nombre.lower())

    for key in list(dic.keys()):
        if nombre in accent(key.lower()):
            eliminado = dic.pop(key)
            return True, f"Se eliminó el contacto: \n{key} (+{eliminado})"
    
    return False, "No se encontró ese contacto"

def edit_contact(dic, nombre_actual, nuevo_nombre=None, nuevo_telefono=None):
    """
    Edita un contacto existente.
    Puede cambiar nombre, teléfono o ambos.
    """
    if nombre_actual not in dic:
        return False, "Ese contacto no existe"
    
    telefono_original = dic[nombre_actual]

    # Actualzar nombre
    if nuevo_nombre:
        nuevo_nombre = nuevo_nombre.strip()
        dic[nuevo_nombre] = telefono_original
        del dic[nombre_actual]
        nombre_actual = nuevo_nombre
    
    # Actualizar telefono
    if nuevo_telefono:
        if not nuevo_telefono.isdigit():
            return False, "El teléfono nuevo debe ser numérico"
        dic[nombre_actual] = int(nuevo_telefono)

    return True, "Contacto actualizado correctamente"

def search_contact(dic,nombre):
    """
    Retorna lista de coincidencias para el buscador.
    """
    nombre = accent(nombre.lower())
    resultados = []

    for key, value in dic.items():
        if nombre in accent(key.lower()):
            resultados.append((key,value))
    
    return resultados