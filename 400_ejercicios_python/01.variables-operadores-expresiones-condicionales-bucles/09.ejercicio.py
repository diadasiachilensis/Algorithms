#Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe mostrar sus valores multiplicados del 1 al 9 inclusive
def main():
    for i in range(1, 11):
        print("tabla de multiplicar del ", i)
        for j in range (2,11):
            result=i*j
            print(f"{i} x {j} = {result}")
    print()

if __name__=="__main__":
    main()