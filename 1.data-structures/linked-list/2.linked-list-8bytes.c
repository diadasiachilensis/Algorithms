#include <stdio.h>
#include <stdlib.h>

//Se declara una estructura llamada Node
typedef struct Node {
    
    int data;               //Dato que almacena el nodo
    struct Node* next;      //Puntero al siguiente nodo de la lsita

} Node;


Node* createNode(int data){

    Node* newNode = (Node*)malloc(sizeof(Node));    // Reserva memoria dinámica suficiente para un Node.
    if (!newNode){                                  // Verifica si la reserva de memoria falló (si malloc devolvió NULL).
        printf("Memory allocation failed!");
        exit(1);
    }

    newNode -> data = data;     //Asigna el valor del nodo. Guarda el valor que recibes como argumento.
    newNode -> next =  NULL;    // El siguiente nodo todavia no existe. Inicializa el puntero al siguiente nodo en NULL, porque este nodo aún no apunta a otro.
    
    return newNode;             //Devuelve la dirección del nuevo nodo creado en memoria.

}

