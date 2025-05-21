def detectar(a,list1):
    if a in list1:
        list1.remove(a) # Elimina solo la primera ocurrencia
        return True
    return False # No se encontró el número
          

# lista = [1, 2, 3, 2, 4, 2, 5]
# lista = [x for x in lista if x != 2]
# print(lista)  # ✅ [1, 3, 4, 5]


if __name__ == "__main__":
    # 1️⃣ Caso normal: eliminar un número presente en la lista
    lista1 = [1, 2, 3, 4, 5]
    assert detectar(3, lista1) == True
    assert lista1 == [1, 2, 4, 5]  # ✅ 3 ha sido eliminado

    # 2️⃣ Caso donde el número no está en la lista
    lista2 = [10, 20, 30, 40]
    assert detectar(50, lista2) == False  # ❌ 50 no está en la lista
    assert lista2 == [10, 20, 30, 40]  # ✅ La lista no cambia

    # 3️⃣ Caso con múltiples ocurrencias: solo elimina la primera
    lista3 = [5, 10, 15, 10, 20]
    assert detectar(10, lista3) == True
    assert lista3 == [5, 15, 10, 20]  # ✅ Solo la primera ocurrencia de 10 fue eliminada

    # 4️⃣ Caso con un solo elemento en la lista
    lista4 = [100]
    assert detectar(100, lista4) == True
    assert lista4 == []  # ✅ La lista queda vacía

    # 5️⃣ Caso con una lista vacía
    lista5 = []
    assert detectar(1, lista5) == False  # ❌ No hay elementos que eliminar
    assert lista5 == []  # ✅ La lista sigue vacía

    # 6️⃣ Caso con valores repetidos pero eliminando solo uno
    lista6 = [1, 2, 2, 3, 4, 2, 5]
    assert detectar(2, lista6) == True
    assert lista6 == [1, 2, 3, 4, 2, 5]  # ✅ Solo se eliminó el primer 2

    # 7️⃣ Caso con números negativos
    lista7 = [-1, -2, -3, -2, -4]
    assert detectar(-2, lista7) == True
    assert lista7 == [-1, -3, -2, -4]  # ✅ Solo la primera aparición de -2 fue eliminada

    # 8️⃣ Caso con mezcla de enteros y ceros
    lista8 = [0, 1, 2, 3, 0, 4]
    assert detectar(0, lista8) == True
    assert lista8 == [1, 2, 3, 0, 4]  # ✅ Eliminó solo el primer 0

    # 9️⃣ Caso con valores duplicados en secuencia
    lista9 = [8, 8, 8, 8, 8]
    assert detectar(8, lista9) == True
    assert lista9 == [8, 8, 8, 8]  # ✅ Solo eliminó un 8

    # 🔟 Caso con una lista de gran tamaño
    lista10 = list(range(1000))  # Lista de 0 a 999
    assert detectar(500, lista10) == True
    assert 500 not in lista10  # ✅ Se eliminó el 500, pero los demás números siguen intactos

    print("✅ Todas las pruebas pasaron correctamente.")