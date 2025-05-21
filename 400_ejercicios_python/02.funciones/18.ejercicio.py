
def calcular_maxmin(lista):
    print("El número mayor es: ",max(lista))
    print("El número menor es: ",min(lista))

def tomar_numeros(total):
    lista=[]
    for i in range(total):
        num=int(input(f"Introduce el número {i}: "))
        lista.append(num)
    return calcular_maxmin(lista)

if __name__ == "__main__":
    n=int(input("Introduce la cantidad de números a ingresar: "))
    tomar_numeros(n)