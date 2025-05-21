class Perro:
    def __init__(self,nombre,edad,raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
    
    def ladrar(self):
        print(f"El perro {self.nombre} esta ladrando")

    def informacion(self):
        print(f"El perro {self.nombre} es de raza {self.raza} y tiene una edad de {self.edad} anhos")