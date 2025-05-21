class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def encender(self):
        print(f"El vehiculo {self.marca} {self.modelo} esta encendido")
    
    def apagar(self):
        print(f"El vehiculo {self.marca} {self.modelo} esta apagado")