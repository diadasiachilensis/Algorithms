class Contacto:
    def __init__(self, nombre, apellido, correo, telefono, data, id):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.data = []

    def add_data(self, nombre, apellido, correo, telefono, id):
        self.data.append({'Nombre': nombre, 'Apellido': apellido, 'correo': correo, 'telefono': telefono, 'id': id})

    def mod_user(self):
        try:
            id_look = int(input("Introduce el id para desarrollar modificaciones: "))
        except ValueError:
            print("El ID debe ser un número.")
            return

        for data in self.data:
            if data['id'] == id_look:
                while True:
                    print("""
¿Qué desea modificar?
1. Nombre
2. Apellido
3. Correo
4. Teléfono
5. Salir
""")
                    opcion = input("Seleccione una opción: ")

                    if opcion == '1':
                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                        data['Nombre'] = nuevo_nombre
                        print("Nombre modificado correctamente.")
                    elif opcion == '2':
                        nuevo_apellido = input("Ingrese el nuevo apellido: ")
                        data['Apellido'] = nuevo_apellido
                        print("Apellido modificado correctamente.")
                    elif opcion == '3':
                        nuevo_correo = input("Ingrese el nuevo correo: ")
                        data['correo'] = nuevo_correo
                        print("Correo modificado correctamente.")
                    elif opcion == '4':
                        nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                        data['telefono'] = nuevo_telefono
                        print("Teléfono modificado correctamente.")
                    elif opcion == '5':
                        print("Saliendo del menú de modificación.")
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")
                return  # Salir del método después de modificar
        print("No se encontró un contacto con ese ID.")
