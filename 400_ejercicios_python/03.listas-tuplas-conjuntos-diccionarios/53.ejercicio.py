"""
53)Diccionario Anidado: Trabaja con un diccionario anidado que represente datos de una tienda, como productos y precios.
"""
tienda = {
    "informacion": {
        "nombre": "Minimarket Los Aromos",
        "direccion": "Av. Las Flores 234, Santiago",
        "horario": "08:00 - 21:00",
        "telefono": "+56 9 5555 4444",
        "propietario": "Carlos Morales",
        "año_apertura": 2015,
        "sucursal": "Las Condes",
        "metodos_pago": ["efectivo", "tarjeta", "transferencia"],
        "redes_sociales": {
            "instagram": "@losaromos_market",
            "facebook": "facebook.com/losaromosmarket"
        },
        "licencia_sanitaria": {
            "numero licencia sanitaria": "LS-2033-CH",
            "vigencia licencia sanitaria": "2026-12-31"
        }
    },

    # 🛒 PRODUCTOS Y SU DETALLE
    "productos": {
        "manzanas": {
            "precio": 890,
            "stock": 35,
            "categoria": "frutas",
            "unidad": "kg",
            "proveedor": "Frutícola del Sur",
            "fecha_ingreso": "2025-10-01",
            "fecha_vencimiento": "2025-10-20",
            "descuento": 0,
            "oferta": False,
            "ventas_mensuales": 45
        },
        "pan": {
            "precio": 1500,
            "stock": 20,
            "categoria": "panadería",
            "unidad": "unidad",
            "proveedor": "Panadería Don Luis",
            "fecha_ingreso": "2025-10-10",
            "fecha_vencimiento": "2025-10-17",
            "descuento": 10,
            "oferta": True,
            "ventas_mensuales": 80
        },
        "leche": {
            "precio": 1200,
            "stock": 15,
            "categoria": "lácteos",
            "unidad": "litro",
            "proveedor": "Lácteos del Valle",
            "fecha_ingreso": "2025-10-05",
            "fecha_vencimiento": "2025-11-05",
            "descuento": 0,
            "oferta": False,
            "ventas_mensuales": 60
        },
        "arroz": {
            "precio": 1350,
            "stock": 40,
            "categoria": "abarrotes",
            "unidad": "kg",
            "proveedor": "Granos Chile",
            "fecha_ingreso": "2025-09-28",
            "fecha_vencimiento": "2026-09-28",
            "descuento": 5,
            "oferta": True,
            "ventas_mensuales": 110
        },
        "huevos": {
            "precio": 2500,
            "stock": 10,
            "categoria": "proteínas",
            "unidad": "docena",
            "proveedor": "Avícola El Alba",
            "fecha_ingreso": "2025-10-02",
            "fecha_vencimiento": "2025-11-02",
            "descuento": 0,
            "oferta": False,
            "ventas_mensuales": 30
        },
        "detergente": {
            "precio": 2990,
            "stock": 25,
            "categoria": "limpieza",
            "unidad": "litro",
            "proveedor": "Limpiamax S.A.",
            "fecha_ingreso": "2025-09-20",
            "fecha_vencimiento": "2027-09-20",
            "descuento": 15,
            "oferta": True,
            "ventas_mensuales": 20
        }
    },

    # 👷 EMPLEADOS
    "empleados": {
        "empleado_1": {
            "nombre": "María López",
            "cargo": "Cajera",
            "horario": "08:00 - 16:00",
            "sueldo": 620000,
            "antigüedad": 3,
            "contacto": "+56 9 9988 7766"
        },
        "empleado_2": {
            "nombre": "Pedro Castillo",
            "cargo": "Reponedor",
            "horario": "10:00 - 18:00",
            "sueldo": 580000,
            "antigüedad": 2,
            "contacto": "+56 9 6655 4433"
        },
        "empleado_3": {
            "nombre": "Ana Torres",
            "cargo": "Administradora",
            "horario": "09:00 - 17:00",
            "sueldo": 850000,
            "antigüedad": 5,
            "contacto": "+56 9 3344 2211"
        }
    },

    # 🚚 PROVEEDORES
    "proveedores": {
        "Frutícola del Sur": {
            "productos_suministrados": ["manzanas"],
            "contacto": "+56 9 7788 9900",
            "frecuencia_entrega": "semanal",
            "estado": "activo"
        },
        "Panadería Don Luis": {
            "productos_suministrados": ["pan"],
            "contacto": "+56 9 1234 5678",
            "frecuencia_entrega": "diaria",
            "estado": "activo"
        },
        "Lácteos del Valle": {
            "productos_suministrados": ["leche"],
            "contacto": "+56 9 2345 6789",
            "frecuencia_entrega": "semanal",
            "estado": "activo"
        },
        "Granos Chile": {
            "productos_suministrados": ["arroz"],
            "contacto": "+56 9 5678 4321",
            "frecuencia_entrega": "mensual",
            "estado": "activo"
        },
        "Avícola El Alba": {
            "productos_suministrados": ["huevos"],
            "contacto": "+56 9 8765 1234",
            "frecuencia_entrega": "semanal",
            "estado": "activo"
        },
        "Limpiamax S.A.": {
            "productos_suministrados": ["detergente"],
            "contacto": "+56 9 1111 2222",
            "frecuencia_entrega": "mensual",
            "estado": "activo"
        }
    },

    # 🧾 VENTAS REGISTRADAS
    "ventas": [
        {"fecha": "2025-10-20", "producto": "pan", "cantidad": 5, "total": 6750, "medio_pago": "efectivo", "cliente": "Marcos Díaz"},
        {"fecha": "2025-10-21", "producto": "leche", "cantidad": 3, "total": 3600, "medio_pago": "tarjeta", "cliente": "Ana Pérez"},
        {"fecha": "2025-10-21", "producto": "arroz", "cantidad": 2, "total": 2565, "medio_pago": "transferencia", "cliente": "Luis Castro"},
        {"fecha": "2025-10-22", "producto": "detergente", "cantidad": 1, "total": 2541, "medio_pago": "tarjeta", "cliente": "Rosa Herrera"}
    ],

    # 👥 CLIENTES FRECUENTES
    "clientes": {
        "cliente_1": {
            "nombre": "Marcos Díaz",
            "total_compras": 15,
            "fecha_ultima_compra": "2025-10-20",
            "preferencias": ["pan", "leche"],
            "telefono": "+56 9 9987 6655"
        },
        "cliente_2": {
            "nombre": "Ana Pérez",
            "total_compras": 20,
            "fecha_ultima_compra": "2025-10-21",
            "preferencias": ["leche", "arroz"],
            "telefono": "+56 9 8877 5544"
        },
        "cliente_3": {
            "nombre": "Luis Castro",
            "total_compras": 8,
            "fecha_ultima_compra": "2025-10-21",
            "preferencias": ["arroz", "huevos"],
            "telefono": "+56 9 7766 4433"
        }
    }
}

""" ------ 🧩 2. Recorrido de elementos ------"""
# Recorrer todos los productos para mostrar su información (nombre, precio, stock).
def show_products(tienda):
    print("Lista de prodcutos y su información:\n")
    for nombre, datos in tienda["productos"].items():
        print(f"- {nombre.capitalize()}: Precio ${datos['precio']} | Stock: {datos['stock']}")

# Recorrer únicamente las claves o los valores.
def scroll_key_values(tienda):
    print("📦 atributos de los productos:")
    for clave in tienda["productos"].keys():
        print(f"- {clave}")
    
    print("\n💰 Valores de productos:")
    for valor in tienda["productos"].values():
        print(valor)

# Recorrer tanto claves como valores de todos los niveles (bucles anidados).
def scroll_all_levels(tienda):
    print("🔍 Información detallada de cada producto:\n")
    for nombre, datos in tienda["productos"].items():
        print(f"🧾 Producto: {nombre.capitalize()}")
        for atributo, valor in datos.items():
            print(f"   - {atributo}: {valor}")
        print("-"*50)

# Obtener todas las categorías de productos disponibles.
def get_categories(tienda):
    categorias = set()
    for datos in tienda["productos"].values():
        categorias.add(datos["categoria"])
    print(f"🏷️ Categorías disponibles: {', '.join(categorias)}")



""" ------ 🧭 1. Acceso a datos ------ """
#Acceder a una categoría específica (por ejemplo, la información de la tienda).
def info_shop(tienda):
    print("📦 Accediendo a la categoría 'informacion'...\n")
    print("Elija su opción para acceder a la información:\n")
    for key in tienda["informacion"].keys():
        print(f" - {key.capitalize()}")
    while True:
        try:
            selection = input("\nEscriba su opción: ").lower()
            if selection in tienda["informacion"]:
                print(f"\n✅ {selection.capitalize()} es: {tienda['informacion'][selection]}")
                return False
            else:
                print("⚠️ Selección incorrecta. Escriba una opción válida.\n")
        except Exception as e:
            print("❌ Error:", e)
            print("Escriba su opción de manera correcta.")
            return True

# Acceder a un producto específico dentro de productos.
def products(tienda):
    

#Consultar un atributo concreto (precio, stock, categoría).
# Verificar si una clave existe dentro de los niveles del diccionario.





# 🧩 2. Recorrido de elementos
# Recorrer todos los productos para mostrar su información (nombre, precio, stock).
# Recorrer únicamente las claves o los valores.
# Recorrer tanto claves como valores de todos los niveles (bucles anidados).
# Obtener todas las categorías de productos disponibles.

# 🔧 3. Modificación de datos
# Atualizar el precio o stock de un producto.
# Cambiar el número telefónico o dirección de la tienda.
# Añadir un nuevo producto al diccionario.
# Eliminar un producto existente.
# Cambiar el nombre de una categoría o agregar una nueva categoría.

# 📊 4. Análisis y cálculos
# Calcular el valor total del inventario (precio × stock por producto).
# Encontrar el producto más caro o el más barato.
# Determinar qué producto tiene más o menos stock.
# Filtrar productos según una condición (por ejemplo, stock bajo o categoría específica).
# Calcular el promedio de precios o stocks.

# 📦 5. Estructuras derivadas
# Crear una lista o diccionario nuevo solo con algunos datos (por ejemplo, precios).
# Generar un informe con resumen de cada producto.
# Transformar los datos del diccionario a una lista de tuplas o listas anidadas.
# Exportar la información a otros formatos (como JSON o texto plano).

# 🧠 6. Operaciones lógicas
# Verificar si un producto pertenece a cierta categoría.
# Comprobar si hay productos con stock bajo y emitir alertas.
# Evaluar condiciones con if anidados para decisiones (por ejemplo, aplicar descuentos).

# 🧰 7. Limpieza o mantenimiento
# Eliminar claves o productos que no se venden más.
# Reordenar los productos según precio o stock.
# Normalizar los nombres de productos (minúsculas, sin espacios, etc.).

