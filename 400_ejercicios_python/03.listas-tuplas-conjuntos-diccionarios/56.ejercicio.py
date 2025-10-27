"""
56)Diccionario Vacío: Verifica si un diccionario está vacío o no.
"""

def check_dictionary(diccionario):
    try:
        if not diccionario:
            print("⚠️ El diccionario está vacío.")
            return True
        else:
            print("✅ El diccionario contiene datos.")
            return False
    except Exception as e:
        print("❌ Error:", e)
        return None


dic_vacio = {}
dic_datos = {"nombre": "Araucaria", "edad": 2520}

check_dictionary(dic_vacio)
check_dictionary(dic_datos)
