def factorial(n):
    if n==0:
        return 1
    elif n ==1:
        return 1
    elif n>0:
        return n*factorial(n-1)

if __name__=="__main__":
    numero = int(input("Introduce un número: "))
    print(factorial(numero))