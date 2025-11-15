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

def add_contact(dic): 
    try:
        # --- Nombre ---
        nombre = detect_str(input("Ingrese el nombre de la persona: ").strip(),"nombre")
        # --- Apellido ---
        apellido = detect_str(input(f"Ingrese el apellido de la persona: ").strip(),"apellido")
        telefono = detect_str(input("Ingrese teléfono sin +: ").strip(), "teléfono")
        
        # --- Ingreso de datos ---
        key = f"{nombre} {apellido}"
        
        print(f"\n✅ Contacto agregado exitosamente:\n👤 {nombre} {apellido}\n📞 +{telefono}\n") # con salto de linea
    except ValueError as e :
        print(f"⚠️ Entrada inválida. Debe ingresar los datos de manera correcta.\n Error inesperado {e}")
    return 

def edit_contact(dic):
    print("========= ✏️ EDICIÓN DE CONTACTOS ✏️ =========")
    buscado = accent(detect_str(input("Ingrese el nombre del contacto que desea cambiar: ").strip(), "nombre"))
    if buscado not in dic:
        print("❌ Ese contacto NO existe.")
        return menu(dic)
    
    nombre, apellido = buscado.split(" ", 1)

    def editar_nombre():
        new_name = detect_str(input("Ingrese el nuevo nombre: ").strip(), "nombre")
        new_contact = f"{new_name} {apellido}"
        dic[new_contact] = dic.pop(buscado)
        print(f"✅ Nombre actualizado → {new_contact}")
        return menu(dic)
    
    def editar_apellido():
        new_last = detect_str(input("Ingrese el nuevo apellido: ").strip(), "apellido")
        new_contact = f"{nombre} {new_last}"
        dic[new_contact] = dic.pop(buscado)
        print(f"✅ Apellido actualizado → {new_contact}")
        return menu(dic)

    def editar_telefono():
        new_phone = detect_int(input("Ingrese el nuevo teléfono: ").strip(), "teléfono")
        dic[buscado] = new_phone
        print(f"📞 Número actualizado → +{new_phone}")
        return menu(dic)

    def cancelar():
        print("🛑 Edición cancelada.")
        return menu(dic)

    #Menu de edición con diccionario 
    opciones = {
        1 : editar_nombre,
        2 : editar_apellido,
        3 : editar_telefono,
        4 : cancelar
    }

    try:
        opcion = int(input("""
========= ✏️ EDICIÓN DE CONTACTOS ✏️ =========
1. Nombre
2. Apellido
3. Número de teléfono
4. Cancelar
===============================================
Seleccione una opción (1-4): """).strip())
        if opcion in opciones:
            return opciones[opcion]()
        else:
            print("⚠️ Opción inválida.")
            return menu(dic)
        
    except ValueError:
        print("⚠️ Ingrese un número válido.")
        return menu(dic)

def del_contact(dic):
    print("========= 🗑️ ELIMINAR CONTACTO 🗑️ =========")
    buscado = accent(detect_str(input("Ingrese el nombre a eliminar: ").strip(), "nombre")).lower()

    contacto = None

    for key in dic:
        partes = accent(key.lower()).split()
        if buscado in partes:
            contacto = key
            break

    if contacto:
        print(f"👤 {contacto} | 📞 +{dic[contacto]}")
        opcion = input("¿Eliminar? (s/n): ").strip().lower()
        if opcion == "s":
            dic.pop(contacto)
            print("🗑️ Contacto eliminado.")
        else:
            print("🛡️ Acción cancelada.")
    else:
        print(f"❌ No existe un contacto que coincida con: {buscado}")

    return menu(dic)

def show_contact(dic):
    print("========= 📇 AGENDA DE CONTACTOS 📇 =========")

    for key, value in dic.items():
        print(f"👤 {key} → 📞 +{value}")

    print(f"\n📊 Total de contactos: {len(dic)}")
    return menu(dic)

def search_contact(dic):
    print("========= 🔎 BÚSQUEDA DE CONTACTOS 🔍 =========")
    buscado = accent(detect_str(input("Ingrese nombre a buscar: ").strip(), "nombre")).lower()

    encontrado = False 

    for key in dic:
        partes = accent(key.lower()).split()
        if buscado in partes:
            encontrado = True
            print(f"👤 {key} | 📞 +{dic[key]}")

    if not encontrado:
        print("❌ No se encontró ningún contacto con ese nombre.")

    return menu(dic)

def salir():
    print("👋 Saliendo del programa...")
    exit()


agenda = {
    "Carlos Muñoz": 56987654321,
    "María González": 56965432109,
    "Pedro Ramírez": 56991234567,
    "Fernanda Torres": 56999887766,
    "Javier Soto": 5688776655,
    "Camila Reyes": 56993456789,
    "Ignacio Paredes": 56992345678,
    "Sofía Díaz": 56994567890,
    "Andrés Fuentes": 56996789012,
    "Valentina Araya": 56993451200,
    "Tomás Herrera": 56997894321,
    "Constanza Vega": 56990012345,
    "Felipe Navarro": 56992348765,
    "Daniela López": 56991112222,
    "Rodrigo Silva": 56995556666
}