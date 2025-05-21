"""Idem anterior con este dibujo
* * * * *
* * * *
* * *
* *
*"""
def main(filas):
    
    for i in range(filas,0,-1):
        for j in range(i):
            print("*", end="")
        print()

if __name__=="__main__":
    main(5)