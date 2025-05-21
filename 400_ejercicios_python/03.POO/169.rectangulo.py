class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho

    def area(self):
        a=self.largo*self.ancho
        print(f"el area es {a}")
    
    def perimetro(self):
        p=2*self.largo+2*self.ancho
        print(f"el perimetro es {p}")
        