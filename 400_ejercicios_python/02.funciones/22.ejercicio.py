#algoritmo de Euclides para calcular el MCD de dos números enteros positivos

def mcd_euclides(a,b):  
    if b==0:
        print(a)
    elif b!=0:
        return mcd_euclides(b,a%b)

if __name__ == "__main__":
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    if num1>num2:
        mcd_euclides(num1,num2)
    else:
        mcd_euclides(num2,num1)