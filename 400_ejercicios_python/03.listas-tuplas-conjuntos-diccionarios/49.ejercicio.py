numeros = {
    "a": 15,
    "b": 42,
    "c": 8,
    "d": 23,
    "e": 56,
    "f": 12,
    "g": 31,
    "h": 5,
    "i": 47,
    "j": 19
}

def min_max(dic):
    print("🔍 Iniciando búsqueda de mínimo y máximo...\n")

    # Convertimos el diccionario en una lista de valores
    valores = list(dic.values())
    print(f"⚠️ Transformación diccionario en lista: {valores}\n")

    # Inicializamos mínimo y máximo con el primer valor
    minimo = valores[0]
    maximo = valores[0]

    # Recorremos los valores uno por uno
    for v in valores:
        print(f"➡️ Analizando valor: {v}")

        if v < minimo:
            print(f"   🔻 Nuevo mínimo encontrado: {v} (anterior: {minimo})")
            minimo = v

        if v > maximo:
            print(f"   🔺 Nuevo máximo encontrado: {v} (anterior: {maximo})")
            maximo = v

    print("\n✅ Búsqueda finalizada.")
    print(f"📉 Valor mínimo: {minimo}")
    print(f"📈 Valor máximo: {maximo}")

    return minimo, maximo

# Ejemplo de uso
min_max(numeros)