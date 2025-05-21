def menu():
    print("Trabajo de fracciones\n")
    a=int(input("Ingrese el numerador: "))
    b=int(input("Ingrese el denominador: "))
    fraction(a,b)

def fraction(a, b):
    try: 
        if a>b:
            print(f"Es una fraccion impropia en los numeros racionales\n En decimal es {round(a/b,2)} \n En fraccion impropia {a}/{b} \n En fraccion mixta es {a//b} {a%b}/{b}")
        elif a<b:
            gcd=mcd(a,b)
            print(f"Es una fracccion propia en los numeros racionales: \n En decimal es {round(a/b,2)} \n En fraccion propia {a}/{b} \n En fraccion irreductible es {a//gcd}/{b//gcd}")
    except Exception as e:
        print(f"Error: {e}")
        print("No esta definido")
        print("El resutlado es ±∞")

#se aplica el algortimo de euclides para hallar el maximo comun divisor
def mcd(a,b):
    while b != 0:
        temp = a  # Guardamos el valor original de 'a' en 'temp'
        a = b     # 'a' toma el valor de 'b'
        b = temp % b  # 'b' toma el valor de 'a % b' usando el valor original de 'a' guardado en 'temp'
    return a

if __name__ == "__main__":
    menu()