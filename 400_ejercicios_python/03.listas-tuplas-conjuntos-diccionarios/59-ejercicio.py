"""
59)Diccionario de Contactos: Crea un diccionario de contactos con nombres y números de 
teléfono.
"""
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
    while True: 
        try:
            # --- Nombre ---
            nombre=input("Ingrese el nombre de la persona: ").strip()
            nombre=detect_int(nombre,"nombre")

            # --- Apellido ---
            apellido= input(f"Ingrese el apellido de la persona: ").strip()
            apellido=detect_int(nombre,"apellido")
    
            # --- Telefono ---
            telefono=int(input("ingrese el numero de telefono de la persona sin agregar el +: "))
            telefono=detect_int(telefono,"telefono")

            # --- Ingreso de datos ---
            dic[f"{nombre} {apellido}"] = telefono
            print(f"\n✅ Contacto agregado exitosamente:\n👤 {nombre} {apellido}\n📞 +{telefono}\n") # con salto de linea
        except ValueError as e :
            print(f"⚠️ Entrada inválida. Debe ingresar los datos de manera correcta.\n Error inesperado {e}")
        return menu()


def edit_contact(dic):
    while True:
        try:
            print("========= 🔧 EDICIÓN DE CONTACTOS 🔧 =========")
            buscado = input("Ingrese el nombre del contacto que desea cambiar: ")
            buscado = detect_str(buscado, "nombre")
            if buscado in dic:
                opcion = input("""
========= 🔧 EDICIÓN DE CONTACTOS 🔧 =========
1. Nombre
2. Apellido
3. Número de teléfono
4. Cancelar
===============================================
Seleccione una opción (1-4): """).strip()
                if opcion == 1:
                    new_name = input("Ingrese el nuevo nombre: ").strip()
                    #separar y conservar el numero
                    if " " in buscado:                  # Si hay al menos un espacio en el texto
                        partes   = buscado.split(" ",1)
                        apellido = partes[1]              #toma el segundo dato, el apellido
                    else: 
                        apellido = ""                   # Si no hay espacio, deja apellido vacío
                    new_contact  = f"{new_name} {apellido}".strip()
                    # .pop() elimina la clave antigua y devuelve su valor; se reasigna el mismo número a la nueva clave
                    dic[new_contact]=dic.pop(buscado)   # Mueve el número al nuevo nombre: borra la clave vieja y conserva el valor
                    return menu()
                elif opcion == 2: 
                    new_subname=input("Ingrese el nuevo apellido: ").strip()
                    if " " in buscado:
                        partes   = buscado.split(" ",1)
                        nombre = partes[0]
                    else: 
                        nombre  = ""
                    new_contact = f"{nombre} {new_subname}".strip()
                    dic[new_contact] = dic.pop(buscado)
                    return menu()
                elif opcion == 3:
                    try: 
                        new_phone = input("Ingrese el nuevo numero de telefono: ").strip()
                        new_phone = detect_int(new_phone, "telefono")
                        dic[buscado]=new_contact 
                    except ValueError as e:
                        print(f"⚠️ Entrada inválida. Debe ingresar los datos de manera correcta.\n Error inesperado {e}")
                    return menu()
                elif opcion == 4:
                    return menu()
        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar el nombre de manera correcta.")

def  del_contact(dic):
    while True:
        try: 
            print("========= 🔧 EDICIÓN DE CONTACTOS 🔧 =========")
            
    return menu()
    pass

def show_contact(dic):
    
    return menu()
    pass

def search_contact(dic):

    return menu()
    pass

def salir():
    exit()


def menu():
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
            if opcion < 1 or opcion > 6: 
                print("❌ Error: ingrese un número entre 1 y 6.")
                continue
            else: 
                if opcion == 1:
                    add_contact(agenda)
                elif opcion == 2:
                    edit_contact(agenda)
                elif opcion == 3:
                    del_contact(agenda)
                elif opcion == 4: 
                    show_contact(agenda)
                elif opcion == 5:
                    search_contact(agenda)
                elif opcion == 6: 
                    salir()
        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar un número.")