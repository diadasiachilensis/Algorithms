def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido")

def max(a,b):
    if a > b:
        return a
    else:
        return b


if __name__ == "__main__":
        while True:
            try:
                num1=solicitar_entero("Ingrese el primer número: ")
                num2=solicitar_entero("Ingrese el segundo número: ")
                print(f"El número mayor es: {max(num1,num2)}")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("Ingrese un número válido")