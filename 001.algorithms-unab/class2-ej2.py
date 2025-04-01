def inv_string(cadena):
    pila=[]
    for caracter in cadena:
        pila.append(caracter)
    result=""

    while pila:
        result+=pila.pop()
    return result

print("")