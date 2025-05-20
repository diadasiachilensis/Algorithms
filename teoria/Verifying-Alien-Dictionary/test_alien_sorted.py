import pytest

from alien_dictionary import alien_sorted  # Asumiendo que la función está en alien_dictionary.py

@pytest.mark.parametrize("words, order, expected", [
    # Caso básico ordenado
    (["hola", "holaa", "holb"], "hlabcdefgijkmnopqrstuvwxyz", True),
    # Lista vacía o un solo elemento siempre ordenada
    ([], "abcdefghijklmnopqrstuvwxyz", True),
    (["solo"], "abcdefghijklmnopqrstuvwxyz", True),
    # Prefijo: "app" precede "apple"
    (["app", "apple"], "abcdefghijklmnopqrstuvwxyz", True),
    # No ordenado: diferencia en la primera letra
    (["bello", "apple"], "abcdefghijklmnopqrstuvwxyz", False),
    # No ordenado: misma prefijo, segunda palabra más corta
    (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    # Orden personalizado: 'a' > 'b'
    (["a", "b"], "bacdefghijklmnopqrstuvwxyz", False),
    # Repetición de palabras
    (["test", "test", "test"], "abcdefghijklmnopqrstuvwxyz", True),
    # Orden con caracteres al final
    (["xyz", "z"], "abcdefghijklmnopqrstuvwxyz", True),
])
def test_alien_sorted(words, order, expected):
    assert alien_sorted(words, order) == expected


def test_invalid_characters():
    # Letras no presentes en `order`
    with pytest.raises(KeyError):
        alien_sorted(["hola", "mundo"], "abc")  # 'h' no está en order corto


if __name__ == "__main__":
    pytest.main()
