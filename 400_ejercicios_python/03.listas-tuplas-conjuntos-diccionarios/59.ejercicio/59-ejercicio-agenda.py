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
        dic[f"{nombre} {apellido}"] = telefono
        
        print(f"\n✅ Contacto agregado exitosamente:\n👤 {nombre} {apellido}\n📞 +{telefono}\n") # con salto de linea
    except ValueError as e :
        print(f"⚠️ Entrada inválida. Debe ingresar los datos de manera correcta.\n Error inesperado {e}")
    return menu(dic)

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
    
def menu(dic):
    while True:
        try: 
            opcion = int(input("""
========= MENÚ DE CONTACTOS =========
1. Agregar contacto
2. Editar contacto
3. Eliminar contacto
4. Ver todos los contactos
5. Buscar contacto
6. Salir
====================================
Seleccione una opción (1-6): """))
        
            opciones = {
                1: add_contact,
                2: edit_contact,
                3: del_contact, 
                4: show_contact,
                5: search_contact, 
                6: salir
            }
            
            if opcion in opciones:
                return opciones[opcion](dic)
            else:
                print("⚠️ Opción inválida. Intente nuevamente.")

        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar un número.")

if __name__ == "__main__":
    agenda = {
    "Carlos Muñoz": "56 9 8765 4321",
    "María González": "56 9 6543 2109",
    "Pedro Ramírez": "56 9 9123 4567",
    "Fernanda Torres": "56 9 9988 7766",
    "Javier Soto": "56 9 8877 6655",
    "Camila Reyes": "56 9 9345 6789",
    "Ignacio Paredes": "56 9 9234 5678",
    "Sofía Díaz": "56 9 9456 7890",
    "Andrés Fuentes": "56 9 9678 9012",
    "Valentina Araya": "56 9 9345 1200",
    "Tomás Herrera": "56 9 9789 4321",
    "Constanza Vega": "56 9 9001 2345",
    "Felipe Navarro": "56 9 9234 8765",
    "Daniela López": "56 9 9111 2222",
    "Rodrigo Silva": "56 9 9555 6666"
    }
    menu(agenda)