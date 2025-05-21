def validar_lista(mensaje):
    """Verifica si el argumento es una lista y si todos sus elementos son números."""
    if not isinstance(mensaje, list):
        print("El argumento no es una lista.")
        return False

    # Verifica que todos los elementos sean números (int o float)
    if all(isinstance(elemento, (int, float)) for elemento in mensaje):
        print(f"La lista {mensaje} tiene solamente números.")
        return True
    else:
        print(f"La lista {mensaje} contiene elementos no numéricos.")
        return False

def suma(lista):
    """Devuelve la suma de todos los elementos de la lista."""
    suma=0 
    for i in lista:
        suma+=i
    return suma
    
def multip(lista):
    """Devuelve el producto de todos los elementos de la lista."""
    resultado=1
    for i in lista:
        resultado*=i
    return resultado

def funciones(mensaje):
    """Ejecuta las funciones si la lista es válida."""
    if validar_lista(mensaje):  # Verifica primero que sea una lista válida
        print(f"Suma: {suma(mensaje)}")
        print(f"Multiplicación: {multip(mensaje)}")

if __name__ == "__main__":
    # 🔹 Pruebas con assert
    assert validar_lista([1, 2, 3, 4, 5]) == True
    assert suma([1, 2, 3, 4, 5]) == 15
    assert multip([1, 2, 3, 4, 5]) == 120

    assert validar_lista([-1, -2, -3, -4]) == True
    assert suma([-1, -2, -3, -4]) == -10
    assert multip([-1, -2, -3, -4]) == 24

    assert validar_lista([10, 20, 30]) == True
    assert suma([10, 20, 30]) == 60
    assert multip([10, 20, 30]) == 6000

    assert validar_lista([0, 0, 0]) == True
    assert suma([0, 0, 0]) == 0
    assert multip([0, 0, 0]) == 0  # Producto de ceros es cero

    print("✅ Todas las pruebas pasaron correctamente.")
    # 🔹 Pruebas con assert para listas que NO deben ser válidas (porque contienen elementos no numéricos)
    assert validar_lista(["a", "b", "c", "d"]) == False
    assert validar_lista([True, False, True]) == True
    assert validar_lista(["Hola", 2, 3.5]) == False  # Mezcla de texto y números
    assert validar_lista([None, None, None]) == False
    assert validar_lista([[], {}, ()]) == False  # Diferentes tipos de datos vacíos
    assert validar_lista([[1, 2], [3, 4]]) == False  # Lista anidada con números (debe fallar)
    assert validar_lista([{"clave": "valor"}, {"otro": "dato"}]) == False  # Diccionarios dentro de la lista
    assert validar_lista(["Python", "Java", "C++", "JavaScript"]) == False  # Solo cadenas de texto
    assert validar_lista(["💡", "🎉", "🔥"]) == False  # Emojis en la lista
    assert validar_lista([(1, 2), (3, 4)]) == False  # Lista de tuplas

    print("✅ Todas las pruebas para listas no numéricas pasaron correctamente.")