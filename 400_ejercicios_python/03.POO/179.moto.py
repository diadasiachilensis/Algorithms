class Moto:
    def __init__(self,marca,modelo,anho,t,d,v_i):
        self.marca  = marca
        self.modelo = modelo
        self.anho   = anho
        self.t      = t         #tiempo de desplazamiento
        self.d      = d         #desplazamiento
        self.v_i    = v_i       #velocidad inicial
        self.a      = None
        
    #Si es movimiento uniformente acelerado
    def acel(self):
        if self.v_i == 0:
            self.a = (2*self.d)/self.t**2
        else: 
            self.a = (2*(self.d-self.v_i*self.t))/(self.t**2)
        return self.a

#   10 modelos de motos
motos = [
    Moto("Yamaha", "MT-03", 2023, t=4, d=20, v_i=0),
    Moto("Honda", "CBR500R", 2022, t=5, d=40, v_i=0),
    Moto("Kawasaki", "Ninja 400", 2024, t=6, d=60, v_i=0),
    Moto("Suzuki", "GSX-S750", 2023, t=3, d=18, v_i=2),
    Moto("BMW", "G310R", 2022, t=4, d=28, v_i=3),
    Moto("Ducati", "Monster 797", 2024, t=5, d=55, v_i=4),
    Moto("KTM", "Duke 390", 2023, t=4, d=25, v_i=1),
    Moto("Harley-Davidson", "Iron 883", 2021, t=6, d=70, v_i=5),
    Moto("Triumph", "Street Triple", 2023, t=3, d=15, v_i=0),
    Moto("Aprilia", "RS 660", 2024, t=7, d=90, v_i=6)
]

#   Mostrar aceleraciones
for i, moto in enumerate(motos, start=1):
    print(f"Moto {i}: {moto.marca} {moto.modelo} ({moto.anho})")
    print(f"  Tiempo: {moto.t}s | Desplazamiento: {moto.d}m | Velocidad inicial: {moto.v_i} m/s")
    print(f"  Aceleración: {moto.acel():.2f} m/s²\n")