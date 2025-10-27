"""
54) Contar Vocales: Cuenta cuántas vocales hay en una cadena de texto
y almacena el resultado en un diccionario.
"""

dictionary = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

def count_vocals(dictionary, texto):
    texto = texto.replace(" ", "").lower()
    for i in texto:
        if i in dictionary:          
            dictionary[i] += 1       #“Toma el valor almacenado bajo la clave i, súmale 1, y guarda el nuevo resultado en esa misma clave”
    return dictionary                

texto = "La programación en Python es poderosa y divertida"
resultado = count_vocals(dictionary, texto)

print("📊 Conteo de vocales:")
for vocal, cantidad in resultado.items():
    print(f"{vocal.upper()} : {cantidad}")
