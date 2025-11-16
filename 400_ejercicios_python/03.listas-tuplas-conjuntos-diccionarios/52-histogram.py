"""
52) Calcular Histograma: Crea un histograma de letras a partir de una cadena de texto.
"""

texto = "La programación en Python es poderosa y divertida"

def histogram_dic(texto):
    print("🔍 Iniciando análisis del texto...\n")
    print(f"📘 Texto original: {texto}\n")

    list_word = texto.lower()  # convertimos a minúsculas
    print(f"🔡 Texto transformado a minúsculas: {list_word}\n")

    letra = {}  # diccionario para contar letras

    print("🚀 Iniciando recorrido carácter por carácter...\n")
    for char in list_word:
        print(f"➡️ Caracter actual: '{char}'")

        if char.isalpha():
            if char not in letra:
                letra[char] = 1
                print(f"   🆕 Nueva letra registrada → '{char}' = 1")
            else:
                letra[char] += 1
                print(f"   🔁 Letra '{char}' incrementada → {letra[char]}")
        else:
            print(f"   ⏭️ Caracter ignorado: '{char}' (no es letra)")
        print("-" * 50)

    print("\n✅ Recorrido finalizado.")
    print("📊 Construyendo histograma...\n")

    for k, v in letra.items():
        print(f"{k} : {'*' * v} ({v})")

    print("\n🏁 Proceso completado con éxito.")
    return letra

# Ejemplo de uso
histogram_dic(texto)
