def contador_registrador(lista):
    tupla_completa = []
    for i in lista:
        contador = 0
        for j in lista:
            if j == i:
                contador += 1
        tupla = (i, contador)  # Crear la tupla correctamente
        tupla_completa.append(tupla)  # Agregarla a la lista
    return tupla_completa  # Agregamos return para poder hacer pruebas

# Pruebas con assert

# 1️⃣ Caso básico con números enteros repetidos
assert contador_registrador([1, 2, 2, 3, 3, 3]) == [(1, 1), (2, 2), (2, 2), (3, 3), (3, 3), (3, 3)]

# 2️⃣ Todos los elementos son iguales
assert contador_registrador([4, 4, 4, 4]) == [(4, 4), (4, 4), (4, 4), (4, 4)]

# 3️⃣ Lista con un solo elemento
assert contador_registrador([5]) == [(5, 1)]

# 4️⃣ Lista vacía (debe devolver una lista vacía)
assert contador_registrador([]) == []

# 5️⃣ Lista con caracteres repetidos
assert contador_registrador(['a', 'b', 'a', 'c', 'c', 'c']) == [('a', 2), ('b', 1), ('a', 2), ('c', 3), ('c', 3), ('c', 3)]

# 6️⃣ Lista con valores booleanos (True y False)
assert contador_registrador([True, False, True, True]) == [(True, 3), (False, 1), (True, 3), (True, 3)]

# 7️⃣ Lista con ceros y unos (binarios)
assert contador_registrador([0, 1, 0, 0, 1, 1, 1]) == [(0, 3), (1, 4), (0, 3), (0, 3), (1, 4), (1, 4), (1, 4)]

# 8️⃣ Lista con caracteres únicos y repetidos
assert contador_registrador(['x', 'y', 'z', 'x']) == [('x', 2), ('y', 1), ('z', 1), ('x', 2)]

# 9️⃣ Lista con números grandes y repetidos
assert contador_registrador([100, 200, 100, 300, 100, 200]) == [(100, 3), (200, 2), (100, 3), (300, 1), (100, 3), (200, 2)]

# 🔟 Lista con números decimales
assert contador_registrador([1.1, 2.2, 1.1, 3.3, 3.3]) == [(1.1, 2), (2.2, 1), (1.1, 2), (3.3, 2), (3.3, 2)]

print("¡Todos los tests pasaron exitosamente! 🚀")
print("✅ Todas las pruebas pasaron correctamente.")