"""
63)Registro de Ventas: Crea un programa que registre las ventas diarias de una tienda 
utilizando un diccionario. El diccionario debe contener las fechas como claves y las ventas 
totales como valores. Utiliza una lista para almacenar los detalles de cada venta, que incluyen 
el producto vendido, la cantidad y el precio unitario. 
"""

from optparse import Option


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

def show_sales(dic):
    pass

def show_sales_by_date(dic):
    """
    Mostrar todas las ventas de una fecha específica
    """

    print("Ventas en fechas")
    date_data(dic)
    Option == input("Escriba de manera correcta la fecha que desea conocer sus ventas: ")
    if not Option in dic:
        print("Escriba la fecha de manera correcta")
    else: 
        show_sales(dic)
        print(f"{dic[Option].items()}")


