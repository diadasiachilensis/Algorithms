"""
57)Buscar Clave: Escribe una función que busque una clave en un diccionario 
y devuelva su valor o un mensaje de error si no se encuentra.
"""
def search_key(dic, key):
    if key in dic:
        print(f"✅ Clave encontrada: '{key}' → Precio: ${dic[key]}")
        return dic[key]
    else:
        print(f"❌ La fruta '{key}' no se encuentra en la lista")
        return None


frutas = {
    "manzana": 850,
    "banana": 700,
    "naranja": 950,
    "kiwi": 1200,
    "uva": 1500
}


search_key(frutas, "kiwi")     # Clave existente
search_key(frutas, "sandía")   # Clave inexistente
