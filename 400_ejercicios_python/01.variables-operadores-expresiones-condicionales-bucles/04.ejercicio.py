#Hacer un programa que solicite una edad e imprima “Es mayor” si es mayor de edad , sino que imprima “Es menor”.
def main():
    edad=int(input("Ingrese su edad: "))

    if 100 > edad >= 18:
        print("Es mayor")
    elif 0 < edad <= 18:
        print("Es menor")
    else:
        print("por favor agregue una edad real")

if __name__=="__main__":
    main()