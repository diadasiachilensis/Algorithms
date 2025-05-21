def validar_vocal(mensaje):
    while True:
        try:
            letra=input(mensaje).strip() #elimina espacios en blanco
            if len(letra)==1 and letra.isalpha(): #verifica que sea una sola letra
                return letra
        except ValueError:
            print("Ingrese una letra válida")

def es_vocal(letra):
    if letra.lower() in "aeiou":
        return True
    else:
        return False

if __name__ == "__main__":
    letra=es_vocal(validar_vocal("Ingrese una letra: "))
    print(letra)