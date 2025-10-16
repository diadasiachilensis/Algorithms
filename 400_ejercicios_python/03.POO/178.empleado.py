class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario  
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: $ {self.salario}")              
    def aumentar_salario(self, porcentaje):
            if porcentaje > 0:
                aumento = self.salario * (porcentaje/100)
                self.salario += aumento
                print(f"Se aumento el salario de {self.nombre} en un {porcentaje}% obteniendo un sueldo de $ {self.salario}. ")
            else: 
                print("El porcentaje debe ser positivo")

empleado1 = Empleado("Guillermo Vidal", "Ingeniero de datos", 1800000)

empleado1.mostrar_informacion()

empleado1.aumentar_salario(10)

empleado1.mostrar_informacion()
            