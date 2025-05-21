def crear_lista_simulada(entradas):
    """
    Función para pruebas: Simula la entrada de datos en la lista.
    :param entradas: Lista de números que simulan la entrada del usuario.
    :return: Lista final creada con los valores ingresados.
    """
    list1 = []
    for num1 in entradas:
        if num1 == 0:  # Condición de salida
            break
        list1.append(num1)  # Agregar el número a la lista
    return list1  # Retorna la lista completa

# Casos de prueba con assert

# 1️⃣ Lista con números positivos y el 0 al final
assert crear_lista_simulada([1, 2, 3, 0]) == [1, 2, 3]

# 2️⃣ Lista con números negativos y el 0 al final
assert crear_lista_simulada([-1, -2, -3, 0]) == [-1, -2, -3]

# 3️⃣ Lista con números mixtos (positivos y negativos)
assert crear_lista_simulada([5, -5, 10, -10, 0]) == [5, -5, 10, -10]

# 4️⃣ Lista vacía (el usuario no ingresa nada y solo pone 0)
assert crear_lista_simulada([0]) == []  # Debe devolver una lista vacía

# 5️⃣ Lista con un solo número antes de terminar
assert crear_lista_simulada([99, 0]) == [99]

# 6️⃣ Lista con decimales
assert crear_lista_simulada([1.5, 2.3, 3.7, 0]) == [1.5, 2.3, 3.7]

# 7️⃣ Lista con varios ceros en medio (solo debe detenerse en el primer 0)
assert crear_lista_simulada([8, 0, 9, 10]) == [8]  # Solo 8 debe entrar

# 8️⃣ Lista con ceros intercalados antes del final
assert crear_lista_simulada([1, 0, 2, 3, 0]) == [1]  # Solo el primer 1 es válido

# 9️⃣ Lista con números grandes y pequeños mezclados
assert crear_lista_simulada([1000, 500, 0]) == [1000, 500]

# 🔟 Lista con valores muy pequeños cercanos a 0
assert crear_lista_simulada([0.0001, 0.0005, 0]) == [0.0001, 0.0005]

print("✅ ¡Todas las pruebas pasaron exitosamente! 🚀")
