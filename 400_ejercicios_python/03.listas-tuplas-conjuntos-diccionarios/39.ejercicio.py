"""
Clase: Listas de nombres de estudiantes.
Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario y secundario.
Luego:
- Mostrar todos los nombres sin repeticiones.
- Mostrar qué nombres se repiten entre niveles.
- Mostrar qué nombres de primario no se repiten en secundario.
"""

# --- Listas principales ---
lista_primario = []
lista_secundario = []
nombres_repetidos = []

# --- Función para ingresar nombres de un nivel ---
def ingresar_nombres(lista, nivel):
    while True:
        try:
            print(f"\n-- LISTA {nivel.upper()} --")
            nombre = input("Ingrese el nombre del estudiante (ingrese 'x' para finalizar): ").strip()

            # Finalizar ingreso
            if nombre.lower() == "x":
                break

            # Validar solo letras y espacios
            if all(c.isalpha() or c.isspace() for c in nombre) and nombre != "":
                lista.append(nombre.capitalize())  # Guardar con mayúscula inicial
                print("✅ Nombre ingresado correctamente.")
            else:
                print("⚠️ Ingrese solo letras y espacios.")
        except ValueError as e:
            print(f"⚠️ Error: {e}")
    return lista

# --- Función para comparar y encontrar nombres repetidos ---
def comparar_nombres(lista1, lista2):
    repetidos = list(set(lista1) & set(lista2))
    return repetidos

# --- Función para mostrar todos los nombres sin repeticiones ---
def nombres_sin_repeticiones(lista1, lista2):
    todos = list(set(lista1 + lista2))
    return todos

# --- Función para mostrar nombres únicos de primario ---
def primario_unicos(lista1, lista2):
    unicos = list(set(lista1) - set(lista2))
    return unicos

# --- Menú principal ---
def menu():
    while True:
        try:
            print("\n========== MENÚ DE OPCIONES ==========")
            print("1. Ingresar nombres de estudiantes de nivel PRIMARIO")
            print("2. Ingresar nombres de estudiantes de nivel SECUNDARIO")
            print("3. Mostrar nombres de PRIMARIO")
            print("4. Mostrar nombres de SECUNDARIO")
            print("5. Mostrar todos los nombres sin repeticiones")
            print("6. Mostrar nombres que se repiten entre PRIMARIO y SECUNDARIO")
            print("7. Mostrar nombres de PRIMARIO que no se repiten en SECUNDARIO")
            print("8. Salir")

            opcion = int(input("Seleccione una opción: ").strip())

            if opcion == 1:
                ingresar_nombres(lista_primario, "Primario")
            elif opcion == 2:
                ingresar_nombres(lista_secundario, "Secundario")
            elif opcion == 3:
                print(f"\n👦 Nivel Primario ({len(lista_primario)} alumnos):")
                print(lista_primario if lista_primario else "⚠️ Lista vacía.")
            elif opcion == 4:
                print(f"\n🎓 Nivel Secundario ({len(lista_secundario)} alumnos):")
                print(lista_secundario if lista_secundario else "⚠️ Lista vacía.")
            elif opcion == 5:
                print("\n🧩 Nombres sin repeticiones:")
                print(nombres_sin_repeticiones(lista_primario, lista_secundario))
            elif opcion == 6:
                print("\n🔁 Nombres que se repiten en ambos niveles:")
                print(comparar_nombres(lista_primario, lista_secundario))
            elif opcion == 7:
                print("\n🔹 Nombres de PRIMARIO que no están en SECUNDARIO:")
                print(primario_unicos(lista_primario, lista_secundario))
            elif opcion == 8:
                print("\n👋 Programa finalizado.")
                break
            else:
                print("⚠️ Ingrese una opción válida (1 a 8).")

        except ValueError:
            print("⚠️ Error: Debe ingresar un número válido.")

# --- Ejecutar el programa ---
if __name__ == "__main__":
    menu()