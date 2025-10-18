"""
Ejercicio 40: Obtener domicilios únicos para facturación mensual
------------------------------------------------------------
Dada una lista de compras registradas como tuplas:
(cliente, día, monto, domicilio)

Objetivo:
- Obtener una lista de domicilios únicos donde se deben enviar facturas.
- Mostrar también cada cliente y su dirección, sin repeticiones.
"""

def obtener_domicilios(ventas):
    """
    Recibe una lista de tuplas con las ventas del mes y devuelve
    un diccionario con cada cliente y su domicilio único.
    """
    domicilios = {}  # Diccionario: clave = cliente, valor = domicilio

    for cliente, dia, monto, domicilio in ventas:
        # Si el cliente ya existe, no se sobrescribe el domicilio
        # (solo la primera vez que aparece se guarda)
        if cliente not in domicilios:
            domicilios[cliente] = domicilio

    return domicilios  # Retorna diccionario con cliente: domicilio

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    # Lista de ventas del mes (ejemplo del enunciado)
    ventas = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    # Obtener el diccionario de clientes y domicilios
    resultado = obtener_domicilios(ventas)

    # Mostrar salida formateada
    print("📦 Domicilios únicos para facturación:\n")
    for cliente, domicilio in resultado.items():
        print(f"👤 Cliente: {cliente:20} ➜ 🏠 Domicilio: {domicilio}")
