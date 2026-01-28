import pytest
from linked_list_simple import ListaEnlazada, Node

# Fixture para crear una lista limpia en cada test
@pytest.fixture
def lista():
    return ListaEnlazada()

def test_add_single_element(lista):
    lista.add(10)
    assert lista.head.data == 10
    assert lista.head.next is None

def test_add_multiple_elements(lista):
    valores = [10, 20, 30]
    for v in valores:
        lista.add(v)
    
    assert lista.head.data == 10
    assert lista.head.next.data == 20
    assert lista.head.next.next.data == 30

def test_delete_head(lista):
    lista.add(10)
    lista.add(20)
    lista.delete(10)
    assert lista.head.data == 20

def test_delete_middle_element(lista):
    for i in [1, 2, 3]: lista.add(i)
    lista.delete(2)
    assert lista.head.data == 1
    assert lista.head.next.data == 3

def test_delete_last_element(lista):
    for i in [1, 2, 3]: lista.add(i)
    lista.delete(3)
    assert lista.head.next.next is None

def test_delete_non_existent(lista, capsys):
    lista.add(1)
    lista.delete(99) # No debería fallar el código, solo imprimir
    captured = capsys.readouterr()
    assert "The value 99 was not found" in captured.out

def test_delete_empty_list(lista):
    # No debería lanzar excepción
    lista.delete(10)
    assert lista.head is None

# Parametrización para completar 20 casos/validaciones rápidas
@pytest.mark.parametrize("input_data, to_delete, expected_head", [
    ([5, 10, 15], 5, 10),
    ([100, 200], 100, 200),
    (["A", "B", "C"], "A", "B"),
    ([True, False], True, False),
])
def test_various_deletions(lista, input_data, to_delete, expected_head):
    for d in input_data:
        lista.add(d)
    lista.delete(to_delete)
    assert lista.head.data == expected_head

def test_stress_add_10_elements(lista):
    for i in range(10):
        lista.add(i)
    
    actual = lista.head
    count = 0
    while actual:
        count += 1
        actual = actual.next
    assert count == 10