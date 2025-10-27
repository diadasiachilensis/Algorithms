"""
55) Ordenar Diccionario: Ordena un diccionario por sus claves o valores.
"""

def sort_dictionary(diccionario, ordenar_por="clave", reverso=False):
    """
    Ordena un diccionario por clave o valor.
    
    Parámetros:
    - ordenar_por: 'clave' o 'valor'
    - reverso: True para descendente, False para ascendente
    """
    try:
        if ordenar_por == "clave":
            diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda x: x[0], reverse=reverso))
        elif ordenar_por == "valor":
            diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda x: x[1], reverse=reverso))
        else:
            print("⚠️ Debe especificar 'clave' o 'valor' en el parámetro 'ordenar_por'.")
            return None

        print(f"\n📊 Diccionario ordenado por {ordenar_por} ({'descendente' if reverso else 'ascendente'}):")
        for k, v in diccionario_ordenado.items():
            print(f" - {k} : {v}")
        return diccionario_ordenado

    except Exception as e:
        print("❌ Error:", e)
        return None

productos = {
    "pan": 1500,
    "leche": 1200,
    "arroz": 1350,
    "huevos": 2500,
    "manzanas": 890
}

# Ordenar por clave (ascendente)
sort_dictionary(productos, "clave")

# Ordenar por valor (ascendente)
sort_dictionary(productos, "valor")

# Ordenar por valor (descendente)
sort_dictionary(productos, "valor", reverso=True)
