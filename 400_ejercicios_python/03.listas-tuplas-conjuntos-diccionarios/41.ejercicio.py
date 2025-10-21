"""
--- Ejercicio 41 --

"""
import string                       #modulo string

def lectura(list_strings):
    #es el alfabeto ocupando el modulo string
    alfabeto = string.ascii_lowercase   
    #cada letra empieza con cero
    conteo = {letra:0 for letra in alfabeto}
    #recorrer el texto y sumar ocurrencias 
    for palabra in list_strings:
        for letra in palabra:
            if letra.isalpha():         #solo contar letras
                letra = letra.lower()   #evitar mayúsculas y minúsculas diferentes
                if letra in conteo:
                    conteo[letra] += 1
                else:
                    conteo[letra] = 1
    return conteo
    print(conteo)

palabras = [
    "computadora",
    "programación",
    "biología",
    "análisis",
    "datos",
    "inteligencia",
    "artificial",
    "educación",
    "sistema",
    "algoritmo",
    "aprendizaje",
    "informática",
    "modelo",
    "proyecto",
    "tecnología"
]

print(lectura(palabras))