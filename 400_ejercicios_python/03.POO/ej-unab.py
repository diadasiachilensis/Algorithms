class Estudiante:
    #Clase que define un estudiante
    def __init__(self,rut="12345768-4",nombre="Estudiante",apellido="Estudioso",edad=0,carrera="carrera"):
        self.rut=rut
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.carrera=carrera

    def describe(self):
        print(f"""Estudiante 
        Rut: {self.rut}
        Nombre: {self.nombre} {self.apellido}
        Edad: {self.edad}
        Carrera: {self.carrera}
        """)

est = Estudiante()
est.describe()
est2=Estudiante("23456098-2", "Galindo","Piscola",23)
est2.describe()