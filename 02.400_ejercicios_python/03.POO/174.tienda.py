class Tienda:
    def __init__(self):
        self.productos=[]

    def add_prods(self,producto,precio):
        self.productos.append({'Producto':producto,'valor':precio})
    
    def calcular_total(self):
        total=sum([valor['valor'] for valor in self.productos])
        print(f"El precio total de la compra es: {total}")

#Ejemplo de uso
tienda = Tienda()
tienda.add_prods("camiseta",15000)
tienda.add_prods("blue jeans",40000)

print("Precio total de la compra es: ", tienda.calcular_total())