def validar_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido")

def max_tres(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
if __name__ == "__main__":
    a=validar_int("Ingrese el primer número: ")
    b=validar_int("Ingrese el segundo número: ")
    c=validar_int("Ingrese el tercer número: ")