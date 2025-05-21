import math

def area_per(r):
    p=round(2*math.pi*r,2)
    a=round(math.pi*(r**2),2)
    print(f"el area del circulo es {a} y el perimetro es {p}")

if __name__ == "__main__":
    radio=int(input("Introduce el valor del radio: "))
    area_per(radio)