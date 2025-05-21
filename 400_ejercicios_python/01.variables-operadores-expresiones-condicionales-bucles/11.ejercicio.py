"""Hacer un programa que muestre el siguiente dibujo.
**********
*        *
*        *
*        *
**********"""

def main():
    alto=5
    ancho=10
    print("*"*ancho)
    for _ in range(alto-2):
        print("*"+" "*(ancho-2)+"*")
    print("*"*ancho)
        
if __name__=="__main__":
    main()