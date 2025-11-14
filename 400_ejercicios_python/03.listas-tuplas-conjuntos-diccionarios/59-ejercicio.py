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
            nombre=detect_str(nombre,"nombre")

            # --- Apellido ---
            apellido= input(f"Ingrese el apellido de la persona: ").strip()
            apellido=detect_str(nombre,"apellido")
    
            # --- Telefono ---
            telefono=input("ingrese el numero de telefono de la persona sin agregar el +: ").strip()
            telefono=detect_int(telefono,"telefono")

            # --- Ingreso de datos ---
            dic[f"{nombre} {apellido}"] = telefono
            print(f"\n✅ Contacto agregado exitosamente:\n👤 {nombre} {apellido}\n📞 +{telefono}\n") # con salto de linea
        except ValueError as e :
            print(f"⚠️ Entrada inválida. Debe ingresar los datos de manera correcta.\n Error inesperado {e}")


def edit_contact(dic):
    while True:
        try:
            print("========= ✏️ EDICIÓN DE CONTACTOS ✏️ =========")
            buscado = input("Ingrese el nombre del contacto que desea cambiar: ")
            buscado = detect_str(buscado, "nombre")
            if buscado in dic:
                opcion = input("""
========= ✏️ EDICIÓN DE CONTACTOS ✏️ =========
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

def del_contact(dic):
    while True:
        try: 
            print("========= 🗑️ EDICIÓN DE CONTACTOS 🗑️ =========")
            buscado=input("Ingrese el nombre del contacto que desea eliminar: ").strip()
            buscado=detect_str(buscado,"nombre")
            if buscado in dic:
                print(f"✅ El contacto que desea eliminar existe \n -> El contacto es: \n 👤{buscado} \n Número de telefono 📞 +{dic[buscado]}")
                desicion=input("Desea ejecutar la acción para que el contacto sea eliminad (s/n): ").strip().lower()
                encontrado = True #🚩
                    #Buscar coincidencias parciales
                for i in list(dic.keys()):
                    partes=i.lower().split()
                    if buscado in partes: 
                        encontrado = False #🚩
                        print(f"✅ El contacto que desea eliminar existe \n -> El contacto es: \n 👤{i} \n Número de telefono 📞 +{dic[i]}")
                        while True:
                            if desicion == "s":
                                eliminado=dic.pop(buscado)
                                print(f"🗑️ Se eliminó el contacto {buscado}: {eliminado}")
                                return False
                            elif desicion == "n": 
                                print("🛡️ El contacto no sera eliminado.")
                                return False
                            else: 
                                print("⚠️ Entrada inválida. Ingresa 's' para sí eliminar o 'n' para no eliminar el contacto.")                             
        except ValueError as e: 
            print(f"⚠️ Entrada inválida. Debe ingresar los datos de manera correcta.\n Error inesperado {e}")
    return menu()

def show_contact(dic):
    while True:
        try:
            print("========= 📇 AGENDA DE CONTACTOS 📇 =========")
            for key,value in dic.items():
                print(f"👤 {key} : 📞 +{value}")
            cantidad = len(dic)
            print(f"📊 Total de contactos: {cantidad}")
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}")
        return menu()

def search_contact(dic):

    return menu()
    pass

def salir():
    exit()
    
def menu(command, dic):
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
        
            commands = {
                1: add_contact,
                2: edit_contact,
                3: del_contact, 
                4: show_contact,
                5: search_contact, 
                6: salir
            }
            
            if opcion == 6: 
                print("👋 Saliendo del menú...")
                break
            
            funcion = commands.get(opcion)
            
            if funcion is None:
                print("⚠️ Opción inválida. Intente nuevamente.")
                continue

            funcion(dic)
        
        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar un número.")