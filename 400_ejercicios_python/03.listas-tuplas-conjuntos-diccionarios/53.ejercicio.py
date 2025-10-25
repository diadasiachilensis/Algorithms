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
# Recorrer únicamente las claves o los valores.
# Recorrer tanto claves como valores de todos los niveles (bucles anidados).
# Obtener todas las categorías de productos disponibles.
def iterate_data(option,tienda):
    for k,v in tienda.items():
        if k == option:
            for i,j in v.items():
                return i,j
        return k,v
    



""" ------ 🧭 1. Acceso a datos ------ """
# Acceder a un producto específico dentro de productos.
#Consultar un atributo concreto (precio, stock, categoría).
# Verificar si una clave existe dentro de los niveles del diccionario.
def access_data(tienda):
    print("Información Minimarket Los Aromos\n\tEscriba su opción de la información que desea ingresar:")
    for k in tienda.keys():
        print(f" - {k}")
    while True: 
        try:
            option=input("escriba de forma correcta la información que desea obtener de la tienda: ").lower()
            if "informacion"== option:
                info_shop()
                break
            elif option in ["licencia sanitaria", "licencia_sanitaria"]:
                info_sanitary()
                break
            elif "productos" == option:
                products()
                break
            elif "empleados" == option:
                employees()
                break
            elif "proveedores" == option:
                suppliers()
                break
            elif "ventas" == option:
                sales()
                break
            elif "clientes" == option:
                customers()
                break
            elif option == "salir"
                print("Saliendo del programa ... ")
                break
            else: 
                print("⚠️ Opción no válida. Intente nuevamente.\n")
                return True
        except Exception as e:
            print("❌ Error:", e)
            print("Escriba su opcion de manera correcta")
            return True


        # Acceder a una categoría específica (por ejemplo, la información de la tienda).
        selection = list(tienda["informacion"].keys())
        selection.extend(list(tienda["licencia_sanitaria"].keys()))
        for i in selection:
            print(f"- {i}")
        while True:    
            try: 
                option=input("escriba de forma correcta la información que desea obtener: ").lower()
                for k,v in tienda["informacion"].items(): 
                    if k.lower() == option:
                        print(f"{k.capitalize()} es {v}")
                        return False
            except Exception as e:
                print("❌ Error:", e)
                print("Escriba su opcion de manera correcta")
                return True




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

