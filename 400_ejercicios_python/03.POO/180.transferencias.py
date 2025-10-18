class Banco:
    def __init__(self,id,balance_i=0):
        self.id = id
        self.balance_i = balance_i
        self.cuentas=[]
    
    def agregar_cuenta(self,numero,saldo_inicial):
        nueva_cuenta= {
            'numero' : numero, 
            'saldo'  : saldo_inicial
        }
        self.cuentas.append(nueva_cuenta)
        print(f"Cuenta {numero} creada con saldo inicial de ${saldo_inicial}")
    
    def calcular_saldo(self):
        total=sum([cuenta['saldo'] for cuenta in self.cuentas])
        print(f"El saldo total del banco es: {total}")
        return total
        
    def trans(self,n_emisor, n_receptor, monto):
        #Buscar la cuenta emisora
        cuenta_emisor = None
        for cuenta in self.cuentas:
            if cuenta['numero'] == n_emisor:
                cuenta_emisor = cuenta
                break
        
        #Buscar la cuenta receptora
        cuenta_receptora = None
        for cuenta in self.cuentas:
            if cuenta['numero'] == n_receptor:
                cuenta_receptora = cuenta
                break
        
        #Validar exitencia de las cuentas
        if cuenta_emisor is None or cuenta_receptora is None:
            print("❌ Error: una o ambas cuentas no existen.")
            return
        
        #Validar saldo suficiente
        if cuenta_emisor['saldo'] < monto:
            print(f"❌ Saldo insuficiente en la cuenta {n_emisor}")
            return
        
        #Realizar la transferencia
        cuenta_emisor['saldo']    = cuenta_emisor['saldo'] - monto
        cuenta_receptora['saldo'] = cuenta_receptora['saldo'] + monto 
        
        print(f"✅ Transferencia exitosa de ${monto} desde {n_emisor}")
        print(f"Nuevo saldo de {n_emisor}: ${cuenta_emisor['saldo']}")
        print(f"Nuevo saldo de {n_receptor}: ${cuenta_receptora['saldo']}")


# Ejemplo de uso
banco = Banco("Banco Central")

#Crear cuentas
banco.agregar_cuenta("001", 1000)
banco.agregar_cuenta("002", 1500)

#Realizar una transferencia
banco.trans("001", "002", 200)


print("Saldo total en el banco:", banco.calcular_saldo())