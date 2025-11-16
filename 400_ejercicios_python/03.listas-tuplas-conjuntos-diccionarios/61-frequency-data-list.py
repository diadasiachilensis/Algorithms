"""
61Diccionario de Frequencias: Dada una lista de números, crea un diccionario que muestre 
cuántas veces aparece cada número.
"""
numeros = [
    10, 22, 10, 35, 22, 14, 90, 10, 35, 47, 22, 14, 14, 90, 55, 10,
    22, 47, 47, 81, 35, 10, 14, 22, 90, 81, 55, 47, 10, 22, 35, 14,
    90, 81, 55, 22, 10, 35, 47, 14, 90, 22, 81, 55, 14, 10, 35, 47,
    22, 90, 14, 81, 55, 35, 47, 14, 10, 22, 35, 47, 90, 81, 55, 14,
    10, 22, 35, 90, 47, 14, 81, 55, 10, 35, 22, 47, 90, 14, 81, 55
]

def frequency(numeros):
    print("🔍 Identificando frecuencia de datos...\n")

    frecuencia = {} #diccionario para contar numeros

    print("🚀 Iniciando recorrido dato por dato...\n")
    for num in numeros:
        print(f"➡️ Caracter actual: '{num}'")

        if num not in frecuencia:
            frecuencia[num] = 1
            print(f"   🆕 Nuevo número registrado → '{num}' = 1")
        else:
            frecuencia[num] += 1
            print(f"   🔁 Letra '{num}' incrementada → {frecuencia[num]}")
    print("\n✅ Recorrido finalizado.")
    print("\n🏁 Proceso completado con éxito.")
    return frecuencia

resultado = frequency(numeros)
print("📊 Diccionario final de frecuencias:")
print(resultado)






