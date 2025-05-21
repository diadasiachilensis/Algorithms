def palindromo(mensaje):
    """Verifica si una cadena es un palíndromo (se lee igual al revés)."""
    return mensaje == mensaje[::-1]  # Retorna True si es palíndromo, False si no lo es

if __name__ == "__main__":
    # 🔹 Pruebas con assert para palíndromos
    assert palindromo("anilina") == True  # Palíndromo simple
    assert palindromo("reconocer") == True  # Palíndromo simple
    assert palindromo("radar") == True  # Palíndromo corto
    assert palindromo("12321") == True  # Números palindrómicos
    assert palindromo("A Santa at NASA") == False  # No funciona sin normalización
    assert palindromo("No lemon, no melon") == False  # No funciona sin quitar espacios y comas
    assert palindromo("Python") == False  # No es palíndromo
    assert palindromo("Hola") == False  # No es palíndromo
    assert palindromo("") == True  # Caso especial: cadena vacía (se considera palíndromo)
    assert palindromo(" ") == True  # Un solo espacio también es palíndromo

    print("✅ Todas las pruebas pasaron correctamente.")
