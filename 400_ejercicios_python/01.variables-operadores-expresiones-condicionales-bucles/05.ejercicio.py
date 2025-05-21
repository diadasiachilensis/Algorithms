#Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color inválido” si es cualquier otro.
def main():
    color=input("Ingrese un color del semaforo como amrillo, rojo y verde: ")

    if "verde" == color:
        print("Puede pasar")
    elif "amarillo" == color:
        print("Precaución")
    elif "rojo" == color:
        print("No pasar")
    else:
        print("escriba correctamente los colores del semaforo")
        return main()

if __name__=="__main__":
    main()