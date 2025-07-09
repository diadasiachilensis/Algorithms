lista1=[]
def inname1(lista1):

    while True:
        try:
            name=str(input("Ingrese el nombre de pila del estudiante (ingrese x para finalizar): "))
            if name.isalpha() == True: 
                if name.lower() == "x":
                    break     
                #Validar que haya solo letras y espacios
                if all(c.isalpha() or c.isspace() for c in name) and name != "":
                    lista1.append(name)
                    print("✅ Nombre ingresado correctamente")
                else:
                    print("⚠️ Ingrese solo nombres de manera correcta")               
        except ValueError as e:
            print(f"⚠️ Ocurrio un error: {e}")
            print("⚠️ Ingrese los nombres de manera correcta")
    return lista1

def inname2():
     

def menu(option):
    while True:
        try:
            #Menu de opciones
            print("-- LISTAS DE SECUNDARIA --\n")
            print("Seleccione una opción: \n"
                  "1. Ingresar nombres de estudiantes nivel primario\n"
                  "2. Ingresar nombre de estudiantes nivel secundario\n"
                  "3. Obtener lista de los estudiantes de nivel primario\n"
                  "4. Obtener lista de los estudiantes de nivel secundario\n"
                  "5. Obtener lista de los nombres que se repiten en nivel primario y secundario\n"
                  "6. Obtener lista de los nombres que NO se repiten en nivel primario y secundario\n"
                  "7. Salir")
            #Entrada del usuario
            option=int(input("Ingrese su opción: ").strip())
            #Validación de la opción ingresada
            if option < 1 or option > 7: 
                raise ValueError("La opción debe ser un número valido entre el 1 y el 7")
            if not option: 
                raise ValueError("La opción no puede estar vacía")
        except ValueError as e:
            print(f"Ocurrio un error: {e}")
            print("Ingrese los datos del pasajero de manera correcta")
        if option == 1:
                ()
        elif option == 2:
                ()
        elif option == 3:
                ()
        elif option == 4:
                ()
        elif option == 5: 
                ()
        elif option == 6: 
                ()
        elif option == 7:
                ()

#Ejecutar el programa
if __name__ == "__main__":
    menu()
        