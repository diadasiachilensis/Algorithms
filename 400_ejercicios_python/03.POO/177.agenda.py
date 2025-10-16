class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contact(self, nombre, apellido, telefono):
        self.contacts.append({
            'Nombre': nombre,
            'Apellido': apellido,
            'Contacto': telefono
        })

    def list_contact(self):
        if not self.contacts:
            print("No hay contactos en la agenda.")
            return

        print("📒 Lista de contactos:")
        for contact in self.contacts:
            nombre_contacto = f"{contact['Nombre']} {contact['Apellido']} - {contact['Contacto']}"
            print(f"- {nombre_contacto}")

    def search_contact(self):
        wanted = input("Introduce el nombre: ").strip()

        for contact in self.contacts:
            if contact.get('Nombre').lower() == wanted.lower():
                telefono = contact.get('Contacto')
                print(f"📞 Teléfono de {contact['Nombre']} {contact['Apellido']}: {telefono}")
                return telefono

        print("❌ Contacto no encontrado.")
        return None


# Ejemplo de uso
agenda = Agenda()
agenda.add_contact("Juan", "Pérez", "987654321")
agenda.add_contact("Ana", "López", "912345678")

agenda.list_contact()
agenda.search_contact()