"""Hacer un programa que muestre el siguiente dibujo
*
* *
* * *
* * * *
* * * * *"""

def main(filas):
    
    for i in range(1,filas+1):
        for j in range(i):
            print("*", end="")
        print()

if __name__=="__main__":
    main(5)