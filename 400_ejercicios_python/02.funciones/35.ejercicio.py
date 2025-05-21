def generar_n_caracteres(n,a):
    return n*a

if __name__ == "__main__":
    # 🔹 Pruebas con assert para generar_n_caracteres()
    assert generar_n_caracteres(5, "x") == "xxxxx"  # Caso básico
    assert generar_n_caracteres(3, "*") == "***"  # Multiplicación de asteriscos
    assert generar_n_caracteres(0, "a") == ""  # Caso con n = 0 debe devolver cadena vacía
    assert generar_n_caracteres(1, "b") == "b"  # Caso con n = 1 devuelve solo un carácter
    assert generar_n_caracteres(10, "-") == "----------"  # Multiplicación de guiones
    assert generar_n_caracteres(4, "ab") == "abababab"  # Multiplicación de una cadena más larga
    assert generar_n_caracteres(2, "123") == "123123"  # Números en cadena repetidos
    assert generar_n_caracteres(6, " ") == "      "  # Espacios repetidos
    assert generar_n_caracteres(1, "") == ""  # Caracter vacío multiplicado sigue siendo vacío
    assert generar_n_caracteres(0, "") == ""  # Caso borde: 0 repeticiones de cadena vacía

    print("✅ Todas las pruebas pasaron correctamente.")
    