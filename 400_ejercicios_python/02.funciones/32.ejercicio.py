def inversa(mensaje):
    """Devuelve el mensaje invertido."""
    inverso = mensaje[::-1]
    return inverso

if __name__ == "__main__":
    # 🔹 Pruebas con assert
    assert inversa("hola") == "aloh"
    assert inversa("Python") == "nohtyP"
    assert inversa("12345") == "54321"
    assert inversa("!@#$%") == "%$#@!"
    assert inversa("anilina") == "anilina"  # Palíndromo
    assert inversa(" ") == " "  # Un solo espacio
    assert inversa("") == ""  # Cadena vacía
    assert inversa("abcdefg") == "gfedcba"
    assert inversa("Hola Mundo") == "odnuM aloH"
    assert inversa("123 456 789") == "987 654 321"  # Con espacios en medio

    print("✅ Todas las pruebas pasaron correctamente.")