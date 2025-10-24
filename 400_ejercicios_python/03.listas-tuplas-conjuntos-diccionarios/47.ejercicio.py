def contar_palabras(texto):
    # Paso 1: Convertir todo el texto a minúsculas (para evitar diferencias entre "Hola" y "hola")
    texto = texto.lower()

    # Paso 2: Dividir el texto en palabras (usa split)
    palabras = texto.split()

    # Paso 3: Crear un diccionario vacío para contar las palabras
    conteo = {}

    # Paso 4: Recorrer cada palabra y acumular su frecuencia
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    # Paso 5: Mostrar o devolver el resultado
    return conteo

# Ejemplo de uso
frase = "Sol sol brilla fuerte porque el sol ilumina todo"
resultado = contar_palabras(frase)
print(resultado)
