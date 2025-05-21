def buscar_pasajeros(lista_pasajeros,nombre):
    for pasajero in lista_pasajeros:
        if pasajero[0]==nombre:
            if not pasajero[2]:
                print (f"El pasajero {nombre} no se encuentra en la base de datos")
            else: 
                print(f"El pasajero {nombre} se encuentra en la base de datos")
                print(f"El pasajero {nombre} viajara a {pasajero[2]}")
    

pasajeros=[
    ("Manuel Juarez", 19823451,"Liverpool"), 
    ("Silvana Paredes", 22709128, "Buenos Aires"), 
    ("Rosa Ortiz", 15123978,"Glasgow"), 
    ("Luciana Hernandez", 38981374, "Lisboa")
    ] 

paises=[
    ("Buenos Aires","Argentina"), 
    ("Glasgow","Escocia"), 
    ("Lisboa", "Portugal"), 
    ("Liverpool","Inglaterra"),
    ("Madrid","España")
    ]

nombre_buscado="Rosa Ortiz"
buscar_pasajeros(pasajeros,nombre_buscado)

