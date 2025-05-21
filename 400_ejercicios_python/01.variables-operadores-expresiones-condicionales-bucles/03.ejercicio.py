#Hacer un programa que solicite una edad y determine si es mayor de edad.
def main():
    edad=int(input("Ingrese su edad: "))

    if 100 > edad >= 18:
        print("Usted es mayor de edad")
    elif 0 < edad <= 18:
        print("Usted es menor de edad")
    else:
        print("por favor agregue una edad real")
    
if __name__=="__main__":
    main()