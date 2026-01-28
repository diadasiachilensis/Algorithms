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

    def add(self,data):
        new_node = Node(data)

        # Si la lista esta vacia el nodo agregado es la cabeza
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
            # el nuevo nodo es tanto la cabeza como la cola
            return
        
        #en este caso no hay while, por lo tanto pasa de complejidad O(n) a O(1)
                # Enlaza el ultimo nodo hasta encontrar el ultimo nodo
        self.tail.next = new_node # el que era ultimo ahora apunta al nuevo
        self.tail = new_node # el nuevo ahora es el oficial 'ultimo'

    def delete(self,key):
        #verificar si la lista esta vacia
        if self.head is None:
            return 
        
        # El nodo a borrar es la cabeza
        if self.head.data == key:
            self.head = self.head.next
            return
        
        actual_node = self.head

        # mientras haya un sieguiente nodo y ese siguiente no es el que buscan va al siguietne nodo 
        while actual_node.next and actual_node.next.data != key:
            actual_node = actual_node.next

        # si se detiene el bucle, significa que se detuvo el bucle
        if actual_node.next is None:
            print(f"The value {key} was not found")
            print("The proccess has finished")
            return
        
        # para la eliminacion el nodo salta encima dos veces para no leer el dato
        # actual_node.next es el que se borra. actual_node.next.next es el nodo que sobrevive y al que ahora apuntaremos para "saltarnos" al eliminado.
        actual_node.next = actual_node.next.next