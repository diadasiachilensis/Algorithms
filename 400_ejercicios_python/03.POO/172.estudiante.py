class Estudiante:
    def __init__(self, nombre, edad, calificaciones, notas):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones  # Corrección del nombre de la variable
        self.notas = notas

    def promedio(self):
        if len(self.calificaciones) > 0:
            prom = sum(self.calificaciones) / len(self.calificaciones)  # Corrección en el cálculo
            print("El promedio de calificaciones es:", prom)
        else:
            print("No hay calificaciones para calcular el promedio.")

# Ejemplo de uso
estudiante1 = Estudiante("Juan", 18, [85, 90, 78, 92], ["A", "B", "C", "A"])
estudiante1.promedio()
