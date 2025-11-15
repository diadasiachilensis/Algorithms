"""
60)Unir Listas en Diccionario: Convierte dos listas en un diccionario, utilizando una como 
claves y la otra como valores.
"""
def name(one, two):
    dic = {}
    for clave, valor in zip(one,two):
        dic[clave] = valor
    return dic

def name1(one, two):
    # zip() combina las listas elemento por elemento: (one[0], two[0]), (one[1], two[1])...
    return dict(zip(one, two))    

# Lista de números
edad = [10, 25, 37, 48, 59, 63, 72, 88, 91]
# Lista de strings
nombre = ["José", "Emma", "Paolo", "Sofía", "Martina", "Carlos", "Antonia"]

diccionario = name(nombre,edad)
diccionario1 = name1(nombre,edad)

print(diccionario)
print(diccionario1)