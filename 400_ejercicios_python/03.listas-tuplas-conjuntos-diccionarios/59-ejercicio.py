"""
59)Diccionario de Contactos: Crea un diccionario de contactos con nombres y números de 
teléfono.
"""
def add_contact(dic):
    
    return menu()
    pass

def edit_contact(dic):
    
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
            opcion = input("""
========= MENÚ DE CONTACTOS =========
1. Agregar contacto
2. Editar contacto
3. Eliminar contacto
4. Ver todos los contactos
5. Buscar contacto
6. Salir
====================================
Seleccione una opción (1-6): """)
            if not opcion.isnumeric():
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