"""
Algoritmo con complejidad O(n) porque en el metodo `add(self, data)` para 
insertar un nodo al final, haces esto: 
- Se empieza `self.head`
- usas en `while last_node.next:`
Recorre cada dato por lo tanto el tiempo crece de forma lineal
"""

class Node: 
    def __init__(self, data):
        self.data      = data
        self.next      = None

class ListaEnlazada: 
    def __init__(self):
        self.head = None # EL inicio de la lista (Head)

    def add(self,data):
        new_node = Node(data)

        # Si la lista esta vacia el nodo agregado es la cabeza
        if self.head is None:
            self.head = new_node
            return
        
        # Recorrer la lista hasta encontrar el ultimo nodo
        last_node = self.head
        while last_node.next:              # mientras existe un node siguiente este 'while' sera True
            last_node = last_node.next     # redundancia logicas mientras el ultimo y el siuginte ultimo sera el ultimo
        
        # Enlaza el ultimo nodo hasta encontrar el ultimo nodo
        last_node.next = new_node

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