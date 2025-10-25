"""
50)Eliminar Claves: Escribe una función que elimine las claves de un diccionario 
si su valor es mayor que un cierto umbral.
"""
valores = {
    "a": 12,
    "b": 45,
    "c": 7,
    "d": 28,
    "e": 54,
    "f": 33,
    "g": 19,
    "h": 60,
    "i": 41,
    "j": 25
}

def del_key(dictionary,umbral):
    print(f"🔍 Eliminando claves con valor mayor a {umbral}...\n")

    #Nuevo diccionario para guardar los valores 
    nuevo_dic={}
    for key, value in dictionary.items():
        if value > umbral:
            nuevo_dic[key]=value
            print(f"    🔻 {key} con {value} es mayor y se guarda")
            print(f"         ➕ Agregado → {nuevo_dic}")
        else:
            print(f"    🔺 {key} no se guarda por tener un {value} menor. es menor a {umbral} ")
    print("\n✅ Registro finalizado.")
    print(f"📋 Diccionario terminado: {nuevo_dic}")
    return nuevo_dic

del_key(valores,30)