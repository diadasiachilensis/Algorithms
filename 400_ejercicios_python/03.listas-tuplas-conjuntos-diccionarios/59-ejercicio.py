"""
59)Diccionario de Contactos: Crea un diccionario de contactos con nombres y números de 
teléfono.
"""
def add_contact(dic):
    while True: 
        try:
            new_contact= []
            name=input("Ingrese el nombre de la persona: ")
            while name.lower.isalpha(): 
                new_contact.append(name)    
            subname= input("Ingrese el apellido de la persona: ")
            phone=int(input("ingrese el numero de telefono de la persona sin agregar el +: "))
            dic[f'{name} {subname}'] = phone
            print(f"\n✅ Contacto agregado exitosamente:\n👤 {name} {subname}\n📞 +{phone}\n") # con salto de linea
        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar los datos de manera correcta.")
    return menu()
    pass

def edit_contact(dic):
    while True:
        try:
            
        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar el nombre de manera correcta.")
    return menu()
    pass

def  del_contact(dic):
    
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

            

    pass