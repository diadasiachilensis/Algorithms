"""Hacer un programa que muestre el siguiente dibujo.
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *"""

def main():
    alto=5
    ancho=10
    for i in range(alto):
        for j in range (ancho):
            print("*",end="")
        print()
        
if __name__=="__main__":
    main()