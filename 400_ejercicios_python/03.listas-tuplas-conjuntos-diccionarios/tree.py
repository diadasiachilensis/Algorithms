def recorrer_dic_arbol(diccionario, nivel=0):
    sangria = "    " * nivel      # sangría según profundidad
    rama = "├── "                 # símbolo de rama

    for clave, valor in diccionario.items():
        print(f"{sangria}{rama}{clave}")

        # Si el valor es otro diccionario → recursión
        if isinstance(valor, dict):
            recorrer_dic_arbol(valor, nivel + 1)
        else:
            # Muestra el valor simple con más sangría
            print(f"{sangria}    └── {valor}")

def date_data(dic, nivel=1):
    sangria   = "  " * nivel
    rama      = "├── " 
    ramalast = "└── "
    """
    Mostrar todas las fechas registradas
    """
    print("Fechas registradas")
    for clave in dic.keys():
        if not clave == list(dic)[-1]:
            print(f"{sangria}{rama}{clave}")
        else: 
            print(f"{sangria}{ramalast}{clave}")
