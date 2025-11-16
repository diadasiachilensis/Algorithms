"""
62) Diccionario de Traducción:
Programa para traducir palabras (español → inglés) con opciones para agregar,
eliminar, buscar y mostrar traducciones. Usa estructura de menú profesional.
"""

# ===============================
# Diccionario inicial
# ===============================
traduccion = {
    "hola": "hello",
    "adios": "goodbye",
    "perro": "dog",
    "gato": "cat",
    "casa": "house",
    "libro": "book",
    "agua": "water",
    "rojo": "red"
}

# ===============================
# FUNCIONES PRINCIPALES
# ===============================

def traducir(dic):
    palabra = input("Ingrese la palabra en español que desea traducir: ").strip().lower()
    print("🔎 Traducción:", dic.get(palabra, "❌ No encontrada en el diccionario."))


def agregar(dic):
    esp = input("Ingrese la palabra en español: ").strip().lower()
    eng = input("Ingrese su traducción al inglés: ").strip().lower()
    dic[esp] = eng
    print(f"✅ Se agregó: {esp} → {eng}")


def eliminar(dic):
    palabra = input("Ingrese la palabra en español que desea eliminar: ").strip().lower()
    
    if palabra in dic:
        eliminado = dic.pop(palabra)
        print(f"🗑️ Se eliminó: {palabra} → {eliminado}")
    else:
        print("❌ Esa palabra no existe en el diccionario.")


def mostrar(dic):
    print("\n📖 DICCIONARIO COMPLETO:")
    if not dic:
        print("⚠️ Diccionario vacío.")
    else:
        for esp, eng in dic.items():
            print(f" - {esp} → {eng}")


def salir(dic):
    print("👋 Gracias por usar el diccionario de traducción.")
    exit()


# ===============================
# MENÚ (estructura igual a tu ejemplo)
# ===============================

def menu(dic):
    while True:
        try:
            opcion = int(input("""
========= 📘 MENÚ DE TRADUCCIÓN 📘 =========
1. Traducir palabra
2. Agregar traducción
3. Eliminar palabra
4. Mostrar todo el diccionario
5. Salir
============================================
Seleccione una opción (1–5): """))
            
            opciones = {
                1: traducir,
                2: agregar,
                3: eliminar,
                4: mostrar,
                5: salir
            }

            if opcion in opciones:
                return opciones[opcion](dic)
            else:
                print("⚠️ Opción inválida. Intente nuevamente.")

        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar un número.")


# ===============================
# PROGRAMA PRINCIPAL
# ===============================
menu(traduccion)
