def detect_str(valor,dato):
    while not valor.strip().isalpha():
        print(f"⚠️ El {dato} solo debe contener letras.")
        valor=input(f"Ingrese el {dato} de la persona").strip()
    return valor

def  del_contact(dic):
    while True:
        print("========= 🗑️ EDICIÓN DE CONTACTOS 🗑️ =========")
        buscado=input("Ingrese el nombre del contacto que desea eliminar: ").strip().lower()
        buscado=detect_str(buscado,"nombre")

        encontrado = True #🚩

        #Buscar coincidencias parciales
        for i in list(dic.keys()):
            partes=i.lower().split()
            if buscado in partes: 
                encontrado = True #🚩
                print(f"✅ El contacto que desea eliminar existe \n -> El contacto es: \n 👤{i} \n Número de telefono 📞 +{dic[i]}")
                while True:
                    decision = input("¿Desea eliminar el contacto? (s/n): ").strip().lower()
                    if decision == "s":
                        eliminado=dic.pop(i)
                        print(f"🗑️ Se eliminó el contacto {i}: {eliminado}")
                        return True
                    elif decision == "n": 
                        print("🛡️ El contacto no sera eliminado.")
                        return False
                    else: 
                        print("⚠️ Entrada inválida. Ingresa 's' para sí o 'n' para no.")
            
            if not encontrado:
                print(f"❌ No se encontró ningún contacto con el nombre '{buscado}'.")
                opcion = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
                if opcion != "s":
                    print("👋 Operación cancelada por el usuario.")
                    return False              


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
    
del_contact(agenda)