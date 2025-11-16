"""
63)Registro de Ventas: Crea un programa que registre las ventas diarias de una tienda 
utilizando un diccionario. El diccionario debe contener las fechas como claves y las ventas 
totales como valores. Utiliza una lista para almacenar los detalles de cada venta, que incluyen 
el producto vendido, la cantidad y el precio unitario. 
"""

ventas = {
    "2025-01-02": [
        {"producto": "Polera Hombre", "cantidad": 3, "precio_unitario": 12990},
        {"producto": "Pantalón Mujer", "cantidad": 2, "precio_unitario": 19990},
        {"producto": "Zapatos Deportivos", "cantidad": 1, "precio_unitario": 45990}
    ],

    "2025-01-03": [
        {"producto": "Chaqueta Invierno", "cantidad": 1, "precio_unitario": 34990},
        {"producto": "Gorro Lana", "cantidad": 4, "precio_unitario": 5990},
        {"producto": "Bufanda Polar", "cantidad": 2, "precio_unitario": 7990}
    ],

    "2025-01-04": [
        {"producto": "Polera Mujer", "cantidad": 5, "precio_unitario": 11990},
        {"producto": "Short Deportivo", "cantidad": 3, "precio_unitario": 9990},
        {"producto": "Calcetines", "cantidad": 10, "precio_unitario": 1990}
    ],

    "2025-01-05": [
        {"producto": "Zapatillas Niño", "cantidad": 2, "precio_unitario": 24990},
        {"producto": "Vestido Casual", "cantidad": 1, "precio_unitario": 19990},
        {"producto": "Polerón Unisex", "cantidad": 2, "precio_unitario": 22990}
    ],

    "2025-01-06": [
        {"producto": "Camisa Formal", "cantidad": 3, "precio_unitario": 15990},
        {"producto": "Corbata", "cantidad": 4, "precio_unitario": 4990},
        {"producto": "Blazer Mujer", "cantidad": 1, "precio_unitario": 32990}
    ],

    "2025-01-07": [
        {"producto": "Pantalón Jeans", "cantidad": 5, "precio_unitario": 24990},
        {"producto": "Polera Gráfica", "cantidad": 8, "precio_unitario": 9990},
        {"producto": "Chaqueta Ligera", "cantidad": 2, "precio_unitario": 27990}
    ]
}

def date_data(dic, nivel=1):
    """
    Mostrar todas las fechas registradas
        └──Lista las claves del diccionario.
    """
    
    sangria   = "  " * nivel
    rama      = "├── " 
    ramalast = "└── "

    print("📂 Fechas registradas:")
    for clave in dic.keys():
        if not clave == list(dic)[-1]:
            print(f"{sangria}{rama} 📅 {clave}")
        else: 
            print(f"{sangria}{ramalast} 📅 {clave}")

def show_sales(dic, fecha):
    print(f"\n====== 🛒 CONSULTA DE VENTAS POR FECHA {fecha} ======\n")

    ventas = dic.get(fecha, [])# Obtiene las ventas de la fecha; si no existe, devuelve una lista vacía.

    if not ventas:
        print("⚠️ No hay ventas registradas en esa fecha")
        return

    # Mostrar cada venta con formato claro
    for i, venta in enumerate(ventas, start=1):             # start=1 hace que la numeración comience en 1 en vez de 0,

        producto = venta.get("producto", "Desconocido") #Si NO existe, devuelve "Desconocido" (el valor por defecto).
        cantidad = venta.get("cantidad", 0)             #Si "cantidad" no existe dentro de venta, Python devuelve 0.
        precio = venta.get("precio_unitario", 0)

        print(f"🛒 Venta {i}")
        print(f"   ├── Producto: {producto}")
        print(f"   ├── Cantidad: {cantidad}")
        print(f"   └── Precio unitario: $ {precio}\n")

def show_sales_by_date(dic):
    """
    Mostrar todas las ventas de una fecha específica
        └──Filtra por fecha y muestra los productos vendidos..
    """
    print("\n====== 📅 CONSULTA DE VENTAS POR FECHA ======\n")
    
    date_data(dic)
    
    opcion = input("\nIngrese la fecha EXACTA que desea consultar: ").strip()
    
    if opcion not in dic:
        print("⚠️ Fecha no encontrada. Por favor, escriba una fecha válida.")
        return
    else: 
        show_sales(dic,opcion)

def calculate_daily_sales_total(dic):
    """
    Calcular el total de ventas de un día
        └──Suma `cantidad * precio_unitario` de todas las ventas de esa fecha.
    """
    print("\n====== 💰 TOTAL DE VENTAS POR FECHA ======\n")
    
    # Mostrar fechas disponibles
    date_data(dic)
    
    # Pedir fecha al usuario 
    opcion = input("\nIngrese la fecha EXACTA que desea consultar: ").strip()
    
    if opcion not in dic:
        print("⚠️ Fecha no encontrada. Por favor, escriba una fecha válida.")
        return
    
    #Lista del valor calve de diccionarios "ventas" 
    ventas = dic[opcion]

    total=0
    for venta in ventas:
        cantidad = venta.get("cantidad", 0)
        precio = venta.get("precio_unitario", 0)
        total+= cantidad*precio

    print(f"\n💵 Total de ventas del día {opcion}: $ {total}\n")
    return total


def create_sale_entry(dic):
    """
    Agregar una nueva venta
        └──Inserta un nuevo diccionario dentro de la lista del día.
    """
    print("\n====== 🛒 AGREGAR NUEVA VENTA ======\n")

    new_sale={"producto" : "Desconocido", "cantidad" : 0, "precio_unitario" : 0}

    try:
        new_product = str(input("Ingrese el nuevo producto: ").lower().strip())
        if new_product in ventas["producto"]:
            print("⚠️ El producto ya existe.")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            ventas["cantidad"] += cantidad
            return ventas["cantidad"]
        else:
            cantidad = int(input("Ingrese la cantidad vendida: ")).strip()
            precio   = int(input("Ingreso el precio por valor unitario: ")).strip()
            return cantidad, precio
        
    
    except Exception as e:
        print("❌ Error inesperado:", e)




    


    return new_sale     



