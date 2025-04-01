def del_dupli(lista):
    new_list=[]
    for elemento in lista:
        if elemento not in new_list:
            new_list.append(elemento)
    
    return list(set(lista))