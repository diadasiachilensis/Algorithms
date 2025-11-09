"""
58)Eliminar Clave: Elimina una clave específica 
de un diccionario si existe. 
"""
def del_key(dic,key):
    if key in dic:
        valor=dic.pop(key)
        print(f"✅ Clave '{key}' ha sido eliminada → Precio: ${dic[key]}")
    else: 
        print(f"❌ No se encontró la clave '{key}' en el diccionario.")

frutas = {
    "manzana": 850,
    "banana": 700,
    "naranja": 950,
    "kiwi": 1200,
    "uva": 1500
}


del_key(frutas, "kiwi")     # Clave existente
del_key(frutas, "sandía")   # Clave inexistente
print("📋 Diccionario actualizado:", frutas)