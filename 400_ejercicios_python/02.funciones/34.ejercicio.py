def superposion(a, b):
    for i in a:
        for j in b:
            if i==j:
                return True
    return False

if __name__ == "__main__":
    # 🔹 Pruebas con assert para superposicion()
    assert superposion([1, 2, 3], [3, 4, 5]) == True  # Coincide el número 3
    assert superposion([1, 2, 3], [4, 5, 6]) == False  # No hay coincidencias
    assert superposion([], [1, 2, 3]) == False  # Primera lista vacía
    assert superposion([1, 2, 3], []) == False  # Segunda lista vacía
    assert superposion([], []) == False  # Ambas listas vacías
    assert superposion([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == True  # Coincide el 5
    assert superposion(["a", "b", "c"], ["d", "e", "f"]) == False  # Listas de strings sin coincidencias
    assert superposion(["a", "b", "c"], ["c", "d", "e"]) == True  # Coincide "c"
    assert superposion([True, False], [False, False]) == True  # Coincide False
    assert superposion([True, True], [False, False]) == False  # No hay coincidencias

    print("✅ Todas las pruebas pasaron correctamente.")