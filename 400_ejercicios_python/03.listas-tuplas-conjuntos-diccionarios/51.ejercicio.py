"""
51) Invertir Diccionario: Crea una función que invierta las claves y los valores en un diccionario.
"""

dictionary = {
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

def changes_dics(valores):
    nuevo_dic = {}
    print("🔄 Iniciando inversión del diccionario...\n")
    print(f"Diccionario original: {valores}\n")

    # Recorremos cada clave y valor
    for key, value in valores.items():
        print(f"➡️ Clave actual: {key} → Valor actual: {value}")
        print(f"   📦 Insertando en nuevo_dic: clave = {value}, valor = {key}")
        nuevo_dic[value] = key
        print(f"   🔹 Estado actual del nuevo diccionario: {nuevo_dic}\n")

    print("✅ Inversión completada.")
    print(f"📋 Diccionario invertido final: {nuevo_dic}")
    return nuevo_dic

# Llamada de prueba
changes_dics(dictionary)
