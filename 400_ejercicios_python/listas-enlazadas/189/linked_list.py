"""
Algoritmo con complejidad O(1) porque en el metodo `add(self, data)` para 
con puntero `tail` O(1)
- salto directo a la direccion de memoria
- siempre tarda lo mismo
- usa poquito mas de RAM porque guarda la variable `tail`
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ListaEnlazada: 
    def __init__(self):
        self.head = None # EL inicio de la lista (Head)
        self.tail = None # puntero que indica el ultimo nodo

    def reverse(self,data):
        """
        Objetivo: Invertir la lista en un solo recorrido O(n)
        """
        prev = None
        current = self.head

        # Guardamos la antigua cabeza para que al final sea el tail 
        old_head = self.head

        while current:
            # 1. Guardar el siguiente nodo temporalmente
            # 2. Invertir el puintero 'next' del acutual hacia 'prev'
            # 3. Mover 'prev' al lugar 'current'
            # 4. Mover 'current' al que guardaste en el paso 1
            pass

        # No olvidar acutlizar la cabeza y la cola al final
        self.head = self.tail
        self.tail = old_head

    def to_list(self):
        """
        Auxiliar para verificar el resultado facilmente
        """
        res = []
        actual = self.head
        while actual:
            res.append(actual.data)
            actual = actual.next
        return res