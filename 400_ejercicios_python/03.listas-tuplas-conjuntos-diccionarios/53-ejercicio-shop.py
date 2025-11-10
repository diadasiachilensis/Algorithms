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

    # PRODUCTOS Y SU DETALLE
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

    # EMPLEADOS
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

    # PROVEEDORES
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

    # VENTAS REGISTRADAS
    "ventas": [
        {"fecha": "2025-10-20", "producto": "pan", "cantidad": 5, "total": 6750, "medio_pago": "efectivo", "cliente": "Marcos Díaz"},
        {"fecha": "2025-10-21", "producto": "leche", "cantidad": 3, "total": 3600, "medio_pago": "tarjeta", "cliente": "Ana Pérez"},
        {"fecha": "2025-10-21", "producto": "arroz", "cantidad": 2, "total": 2565, "medio_pago": "transferencia", "cliente": "Luis Castro"},
        {"fecha": "2025-10-22", "producto": "detergente", "cantidad": 1, "total": 2541, "medio_pago": "tarjeta", "cliente": "Rosa Herrera"}
    ],

    # CLIENTES FRECUENTES
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

def recorrer_diccionario_visual(diccionario, nivel=0):
    """
    Recorre todos los niveles del diccionario con formato visual tipo árbol.
    Soporta diccionarios y listas dentro de cualquier nivel.
    """
    sangria = "│   " * nivel
    rama = "├── " if nivel > 0 else ""
    
    for clave, valor in diccionario.items():
        print(f"{sangria}{rama}📦 {clave}:")
        
        # Si el valor es un diccionario, recursión profunda
        if isinstance(valor, dict):
            recorrer_diccionario_visual(valor, nivel + 1)

        # Si el valor es una lista, la recorre elemento por elemento
        elif isinstance(valor, list):
            for i, elemento in enumerate(valor, start=1):
                print(f"{sangria}│   ├── 📄 Elemento {i}:")
                if isinstance(elemento, dict):
                    recorrer_diccionario_visual(elemento, nivel + 2)
                else:
                    print(f"{sangria}│   │   🧾 {elemento}")

        # Si el valor no es estructura compleja, lo muestra directamente
        else:
            print(f"{sangria}│   └── 🧾 {valor}")


def access_section(tienda):
    """
    Permite acceder a cualquier sección principal del diccionario.
    Muestra las claves disponibles y permite explorar sus valores.
    """
    print("\n🧭 Acceso a una categoría específica de la tienda:\n")
    try:
        for seccion in tienda.keys():
            print(f" - {seccion.capitalize()}")

        selection = input("\nEscriba el nombre de la categoría a la que desea acceder: ").lower().strip()
        
        if selection not in tienda:
            print("⚠️ Categoría no encontrada. Escriba una opción válida.")
            return True
        
        valor = tienda[selection]
        print(f"\n✅ Ha accedido a la categoría '{selection.capitalize()}':\n")

        # Si es un diccionario o lista, mostrar su contenido con el árbol recursivo
        if isinstance(valor, (dict, list)):
            recorrer_diccionario_visual({selection: valor})
        else:
            print(f"🧾 Valor directo: {valor}")
        return False

    except Exception as e:
        print("❌ Error:", e)
        print("Por favor, escriba correctamente su entrada.")
        return True

def product_attribute(tienda):
    """
    Permite al usuario consultar un atributo específico de un producto.
    Ejemplo: precio, stock, categoría, proveedor, etc.
    """
    print("\n🎯 Consulta de atributos de productos\n")
    try:
        print("Productos disponibles:")
        for producto in tienda["productos"].keys():
            print(f" - {producto.capitalize()}")

        producto_sel = input("\nEscriba el nombre del producto: ").lower().strip()
        if producto_sel not in tienda["productos"]:
            print("⚠️ Producto no encontrado. Intente nuevamente.")
            return True

        print(f"\nAtributos disponibles de '{producto_sel.capitalize()}':")
        for atributo in tienda["productos"][producto_sel].keys():
            print(f" - {atributo.capitalize()}")

        try:
            atributo_sel = input("\nEscriba el atributo que desea consultar: ").lower().strip()
            if atributo_sel in tienda["productos"][producto_sel]:
                valor = tienda["productos"][producto_sel][atributo_sel]
                print(f"\n✅ El atributo '{atributo_sel}' del producto '{producto_sel.capitalize()}' es: {valor}")
                return False
            else:
                print("⚠️ Atributo no encontrado. Revise la ortografía.")
                return True
        except Exception as e:
            print("❌ Error en la selección del atributo:", e)
            return True

    except Exception as e:
        print("❌ Error general:", e)
        print("Por favor, escriba correctamente su entrada.")
        return True


def get_categories(tienda):
    """
    Extrae y muestra todas las categorías únicas de productos disponibles.
    """
    try:
        categorias = {datos["categoria"] for datos in tienda["productos"].values()}
        print(f"\n🏷️ Categorías disponibles: {', '.join(sorted(categorias))}")
        return False
    except Exception as e:
        print("❌ Error al obtener categorías:", e)
        return True

def buscar_clave_ruta(diccionario, clave_buscada, ruta_actual="raíz"):
    """
    Busca una clave dentro de todos los niveles del diccionario anidado.
    Retorna la ruta completa donde se encontró o None si no existe.
    """
    if clave_buscada in diccionario:
        return [f"{ruta_actual} → {clave_buscada}"]

    for clave, valor in diccionario.items():
        if isinstance(valor, dict):
            resultado = buscar_clave_ruta(valor, clave_buscada, f"{ruta_actual} → {clave}")
            if resultado:
                return resultado
        elif isinstance(valor, list):
            for i, elemento in enumerate(valor):
                if isinstance(elemento, dict):
                    resultado = buscar_clave_ruta(elemento, clave_buscada, f"{ruta_actual} → {clave}[{i}]")
                    if resultado:
                        return resultado
    return None

def check_key_route(tienda):
    """
    Función interactiva que permite buscar una clave y muestra la ruta exacta
    en la que se encuentra dentro del diccionario.
    """
    print("\n🔍 Búsqueda recursiva de clave con ruta de ubicación\n")
    try:
        clave = input("Escriba la clave que desea buscar: ").lower().strip()
        ruta = buscar_clave_ruta(tienda, clave)
        if ruta:
            print(f"\n✅ La clave '{clave}' fue encontrada en la ruta:")
            for r in ruta:
                print(f"   📍 {r}")
        else:
            print(f"⚠️ La clave '{clave}' no se encontró en ningún nivel del diccionario.")
        return False
    except Exception as e:
        print("❌ Error:", e)
        print("Por favor, escriba una clave válida.")
        return True


def update_product_data(tienda):
    """
    Permite actualizar el precio o stock de un producto existente.
    Maneja excepciones y valida que el producto exista.
    """
    print("\n🔧 Actualizar precio o stock de un producto\n")
    try:
        print("Productos disponibles:")
        for p in tienda["productos"]:
            print(f" - {p.capitalize()}")

        producto = input("\nIngrese el nombre del producto que desea modificar: ").lower().strip()
        if producto not in tienda["productos"]:
            print("⚠️ Producto no encontrado.")
            return True

        print("\nOpciones disponibles:")
        print(" 1️⃣ Precio")
        print(" 2️⃣ Stock")
        opcion = input("Seleccione el número de la opción a modificar: ").strip()

        if opcion == "1":
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            tienda["productos"][producto]["precio"] = nuevo_precio
            print(f"✅ Precio de '{producto.capitalize()}' actualizado a ${nuevo_precio}.")
        elif opcion == "2":
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            tienda["productos"][producto]["stock"] = nuevo_stock
            print(f"✅ Stock de '{producto.capitalize()}' actualizado a {nuevo_stock} unidades.")
        else:
            print("⚠️ Opción no válida.")
            return True

        return False

    except ValueError:
        print("❌ Error: debe ingresar un número válido para el precio o stock.")
        return True
    except Exception as e:
        print("❌ Error inesperado:", e)
        return True

def update_store_info(tienda):
    """
    Permite cambiar el número telefónico o la dirección de la tienda.
    """
    print("\n🏪 Modificar información de la tienda\n")
    try:
        print("Opciones disponibles:")
        print(" 1️⃣ Dirección")
        print(" 2️⃣ Teléfono")
        opcion = input("Seleccione el número de la opción a modificar: ").strip()

        if opcion == "1":
            nueva_direccion = input("Ingrese la nueva dirección: ").strip()
            tienda["informacion"]["direccion"] = nueva_direccion
            print(f"✅ Dirección actualizada a: {nueva_direccion}")
        elif opcion == "2":
            nuevo_telefono = input("Ingrese el nuevo número telefónico: ").strip()
            tienda["informacion"]["telefono"] = nuevo_telefono
            print(f"✅ Teléfono actualizado a: {nuevo_telefono}")
        else:
            print("⚠️ Opción no válida.")
            return True

        return False

    except Exception as e:
        print("❌ Error:", e)
        return True

def add_new_product(tienda):
    """
    Permite agregar un nuevo producto al diccionario 'productos'.
    Incluye validación y manejo de excepciones.
    """
    print("\n🆕 Añadir un nuevo producto\n")
    try:
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ").lower().strip()
        if nuevo_producto in tienda["productos"]:
            print("⚠️ El producto ya existe.")
            return True

        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock inicial: "))
        categoria = input("Ingrese la categoría: ").lower().strip()
        proveedor = input("Ingrese el proveedor: ").strip()

        tienda["productos"][nuevo_producto] = {
            "precio": precio,
            "stock": stock,
            "categoria": categoria,
            "unidad": "unidad",
            "proveedor": proveedor,
            "fecha_ingreso": "2025-10-26",
            "fecha_vencimiento": "N/A",
            "descuento": 0,
            "oferta": False,
            "ventas_mensuales": 0
        }

        print(f"✅ Producto '{nuevo_producto.capitalize()}' añadido correctamente.")
        return False

    except ValueError:
        print("❌ Error: el precio o stock deben ser números válidos.")
        return True
    except Exception as e:
        print("❌ Error inesperado:", e)
        return True

def delete_product(tienda):
    """
    Elimina un producto del diccionario 'productos' si existe.
    """
    print("\n🗑️ Eliminar un producto existente\n")
    try:
        print("Productos disponibles:")
        for p in tienda["productos"].keys():
            print(f" - {p.capitalize()}")

        producto = input("\nIngrese el nombre del producto a eliminar: ").lower().strip()
        if producto not in tienda["productos"]:
            print("⚠️ Producto no encontrado.")
            return True

        confirm = input(f"¿Está seguro que desea eliminar '{producto}'? (s/n): ").lower().strip()
        if confirm == "s":
            del tienda["productos"][producto]
            print(f"✅ Producto '{producto.capitalize()}' eliminado correctamente.")
        else:
            print("❎ Operación cancelada.")
        return False

    except Exception as e:
        print("❌ Error:", e)
        return True

def modify_category(tienda):
    """
    Permite cambiar el nombre de una categoría existente o agregar una nueva.
    Aplica la modificación recursivamente en los productos.
    """
    print("\n🏷️ Modificar o agregar una categoría\n")
    try:
        categorias = {datos["categoria"] for datos in tienda["productos"].values()}
        print(f"Categorías actuales: {', '.join(categorias)}")

        opcion = input("\nSeleccione una acción (1️⃣ Cambiar nombre / 2️⃣ Agregar nueva): ").strip()

        if opcion == "1":
            antigua = input("Ingrese el nombre de la categoría que desea cambiar: ").lower().strip()
            if antigua not in categorias:
                print("⚠️ Categoría no encontrada.")
                return True
            nueva = input("Ingrese el nuevo nombre de la categoría: ").lower().strip()
            for producto, datos in tienda["productos"].items():
                if datos["categoria"] == antigua:
                    datos["categoria"] = nueva
            print(f"✅ Categoría '{antigua}' cambiada a '{nueva}'.")
        elif opcion == "2":
            nueva = input("Ingrese el nombre de la nueva categoría: ").lower().strip()
            print(f"✅ Nueva categoría '{nueva}' creada (aún sin productos asignados).")
        else:
            print("⚠️ Opción no válida.")
            return True

        return False

    except Exception as e:
        print("❌ Error:", e)
        return True

def menu_principal(tienda):
    """
    Menú principal interactivo para gestionar el diccionario 'tienda'.
    Permite acceder, consultar y modificar datos del minimarket.
    """
    while True:
        print("\n" + "="*60)
        print("🏪  SISTEMA DE GESTIÓN — MINIMARKET LOS AROMOS")
        print("="*60)
        print("Seleccione una opción:\n")
        print("1️⃣  Acceso a datos")
        print("2️⃣  Recorridos y consultas")
        print("3️⃣  Modificación de datos")
        print("4️⃣  Búsqueda recursiva de claves")
        print("5️⃣  Mostrar todo el diccionario")
        print("0️⃣  Salir del programa")
        print("="*60)

        try:
            opcion = input("👉 Ingrese el número de su opción: ").strip()

            # 🧭 1. Acceso directo a secciones
            if opcion == "1":
                menu_acceso_datos(tienda)

            # 📊 2. Consultas y recorridos
            elif opcion == "2":
                menu_recorridos(tienda)

            # 🔧 3. Modificaciones
            elif opcion == "3":
                menu_modificaciones(tienda)

            # 🔍 4. Buscar clave recursivamente
            elif opcion == "4":
                check_key_route(tienda)

            # 🌳 5. Mostrar estructura completa
            elif opcion == "5":
                print("\n📦 Estructura completa del diccionario:\n")
                recorrer_diccionario_visual(tienda)

            elif opcion == "0":
                print("\n👋 Saliendo del sistema... ¡Hasta pronto!\n")
                break

            else:
                print("⚠️ Opción no válida. Intente nuevamente.")

        except KeyboardInterrupt:
            print("\n🛑 Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print("❌ Error inesperado:", e)

def menu_acceso_datos(tienda):
    while True:
        print("\n--- 🧭 ACCESO A DATOS ---")
        print("1️⃣  Acceder a una categoría (información, empleados, etc.)")
        print("2️⃣  Consultar atributo de un producto")
        print("3️⃣  Ver categorías disponibles")
        print("0️⃣  Volver al menú principal")

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                access_section(tienda)
            elif opcion == "2":
                product_attribute(tienda)
            elif opcion == "3":
                get_categories(tienda)
            elif opcion == "0":
                print("↩️ Volviendo al menú principal...\n")
                break
            else:
                print("⚠️ Opción inválida.")
        except Exception as e:
            print("❌ Error:", e)

def menu_recorridos(tienda):
    while True:
        print("\n--- 📊 RECORRIDOS Y CONSULTAS ---")
        print("1️⃣  Mostrar todo el diccionario en formato árbol")
        print("2️⃣  Acceder a productos (nombre, precio, stock)")
        print("3️⃣  Volver al menú principal")

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                recorrer_diccionario_visual(tienda)
            elif opcion == "2":
                access_section(tienda)
            elif opcion == "3":
                print("↩️ Volviendo al menú principal...\n")
                break
            else:
                print("⚠️ Opción inválida.")
        except Exception as e:
            print("❌ Error:", e)

def menu_modificaciones(tienda):
    while True:
        print("\n--- 🔧 MODIFICACIÓN DE DATOS ---")
        print("1️⃣  Actualizar precio o stock de un producto")
        print("2️⃣  Cambiar teléfono o dirección de la tienda")
        print("3️⃣  Añadir nuevo producto")
        print("4️⃣  Eliminar producto existente")
        print("5️⃣  Cambiar o agregar categoría")
        print("0️⃣  Volver al menú principal")

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                update_product_data(tienda)
            elif opcion == "2":
                update_store_info(tienda)
            elif opcion == "3":
                add_new_product(tienda)
            elif opcion == "4":
                delete_product(tienda)
            elif opcion == "5":
                modify_category(tienda)
            elif opcion == "0":
                print("↩️ Volviendo al menú principal...\n")
                break
            else:
                print("⚠️ Opción inválida.")

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    menu_principal(tienda)