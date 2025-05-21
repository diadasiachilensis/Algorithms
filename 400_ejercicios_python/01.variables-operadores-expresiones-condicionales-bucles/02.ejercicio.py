#Hacer un programa que solicite por teclado dos número y muestre la suma , la resta ,la multiplicación y la división de esos números
def main():
    num1=float(input("Introduce el primer numero: "))
    num2=float(input("Introduce el segundo numero: "))
    suma=int(num1+num2)
    resta=int(num1-num2)
    multiplicacion=int(num1*num2)
    if num2 !=0:
        division=round(num1/num2,2)
    else:
        division="No se puede desarrollar la división, porque es indefinido"

    var_local=locals()

    for nombre,valor in var_local.items():
        if nombre!="num1" and nombre!="num2": 
            print("El resultado de {} es {}".format(nombre, valor))
    
if __name__=="__main__":
    main()