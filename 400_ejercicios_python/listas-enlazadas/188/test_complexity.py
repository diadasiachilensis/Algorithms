import pytest
import time
from linked_list_simple import ListaEnlazada as ListaSimple
from linked_list_optimized import ListaEnlazada as ListaOptimizada

def measure_time(lista_clase, n_elements):
    """Función auxiliar para medir el tiempo de inserción."""
    lista = lista_clase()
    start_time = time.perf_counter()
    
    for i in range(n_elements):
        lista.add(i)
        
    end_time = time.perf_counter()
    return end_time - start_time

def test_performance_comparison():
    # Número de elementos para notar la diferencia
    N = 10000 
    
    # Medir O(n) - Simple
    time_simple = measure_time(ListaSimple, N)
    
    # Medir O(1) - Optimizada
    time_optimized = measure_time(ListaOptimizada, N)
    
    print(f"\n--- Resultados de Complejidad (N={N}) ---")
    print(f"Lista Simple (O(n)):     {time_simple:.5f} segundos")
    print(f"Lista Optimizada (O(1)): {time_optimized:.5f} segundos")
    
    # Validación lógica: La optimizada DEBE ser más rápida que la simple
    # En O(n), el tiempo total de N inserciones es en realidad O(N^2)
    # En O(1), el tiempo total de N inserciones es O(N)
    assert time_optimized < time_simple
    
    # Cálculo de mejora
    mejora = (time_simple / time_optimized)
    print(f"¡La versión optimizada fue {mejora:.1f} veces más rápida!")

def test_functional_integrity_simple():
    """Prueba básica para asegurar que la simple sigue funcionando."""
    ls = ListaSimple()
    ls.add(1)
    ls.add(2)
    assert ls.head.data == 1
    assert ls.head.next.data == 2

def test_functional_integrity_optimized():
    """Prueba básica para asegurar que la optimizada mantiene bien los punteros."""
    lo = ListaOptimizada()
    lo.add(1)
    lo.add(2)
    lo.add(3)
    assert lo.head.data == 1
    assert lo.tail.data == 3 # Verifica que el tail apunte al último
    assert lo.head.next.next == lo.tail # Verifica la conexión