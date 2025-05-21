class Banco:
    def __init__(self):
        self.cuentas=[]
    
    def agregar_cuenta(self,numero,saldo):
        self.cuentas.append({'numero':numero,'saldo':saldo})
    
    def calcular_saldo(self):
        total=sum([cuenta['saldo'] for cuenta in self.cuentas])
        print(f"El saldo total del banco es: {total}")


# Ejemplo de uso
banco = Banco()
banco.agregar_cuenta("001", 1000)
banco.agregar_cuenta("002", 1500)

print("Saldo total en el banco:", banco.calcular_saldo())