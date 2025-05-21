#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba
#los dos números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(a,b):
    if a%b ==0:
        print(f"{a} es multiplo de {b}")
    else:
        print(f"{a} NO es multiplo de {b}")

if __name__ == "__main__":
    num1 = int(input("Introduce un número entero: "))
    num2 = int(input("Introduce otro número entero: "))
    EsMultiplo(num1, num2)