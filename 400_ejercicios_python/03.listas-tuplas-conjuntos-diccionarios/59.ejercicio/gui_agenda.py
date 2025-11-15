import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

agenda = {
    "Carlos Muñoz": "56 9 8765 4321",
    "María González": "56 9 6543 2109",
    "Pedro Ramírez": "56 9 9123 4567",
    "Fernanda Torres": "56 9 9988 7766",
    "Javier Soto": "56 9 8877 6655",
    "Camila Reyes": "56 9 9345 6789",
    "Ignacio Paredes": "56 9 9234 5678",
    "Sofía Díaz": "56 9 9456 7890",
    "Andrés Fuentes": "56 9 9678 9012",
    "Valentina Araya": "56 9 9345 1200",
    "Tomás Herrera": "56 9 9789 4321",
    "Constanza Vega": "56 9 9001 2345",
    "Felipe Navarro": "56 9 9234 8765",
    "Daniela López": "56 9 9111 2222",
    "Rodrigo Silva": "56 9 9555 6666"
    }

# ================================
# FUNCIONES DE LA INTERFAZ
# ================================

def mostrar_contactos():
    """Muestra todos los contactos en una ventana emergente."""
    if not agenda:
        messagebox.showinfo("📇 Agenda", "❗ No hay contactos guardados.")
        return
    
    texto = "📒 *Agenda de Contactos*\n\n"
    for nombre, telefono in agenda.items():
        texto += f"👤 {nombre} → 📞 +{telefono}\n"
    
    messagebox.showinfo("📇 Agenda Completa", texto)


def agregar_contacto():
    """Agrega un contacto usando lo que escribió el usuario."""
    nombre = entry_nombre.get().strip()
    telefono = entry_telefono.get().strip()

    if not nombre:
        messagebox.showwarning("⚠️ Error", "❌ El nombre no puede estar vacío.")
        return

    if not telefono.isdigit():
        messagebox.showwarning("⚠️ Error", "📵 El teléfono debe ser numérico.")
        return

    agenda[nombre] = int(telefono)

    messagebox.showinfo("✔️ Éxito", f"Contacto agregado:\n\n👤 {nombre}\n📞 +{telefono}")

    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)

"""
============================
FUNCIONES DE LA GUI
============================
"""
root = tk.Tk()                  # crea la ventana principal
root.title("📱 Agenda")         # le da un nombre
root.geometry("320x300")        # define su tamaño

# ===== Cargar tema Azure =====
root.tk.call("source", "azure.tcl")
style = ttk.Style(root)
style.theme_use("azure")

# ===== Widgets =====

# Etiquetas 
label_nombre = ttk.Label(root, text="📝 Nombre del contacto:")   # Label = texto descriptivo
label_nombre.pack(pady=5)                                        # .pack() lo acomoda automaticamente

# Entry (campo de texto)
entry_nombre = ttk.Entry(root)
entry_nombre.pack(pady=5)              # Lugar donde el usuario escribe

label_telefono = ttk.Label(root, 
                            text = "📞 Teléfono:")
label_telefono.pack()

entry_telefono = ttk.Entry(root)
entry_telefono.pack()

# Botones
btn_agregar = ttk.Button(root,
                        text = "➕ Agregar Contacto",  # Button crea un boton
                        command = agregar_contacto,     # command = le indica que funcion ejecutar cuando lo presionas
                        style = "AccentButton")
btn_agregar.pack(pady = 10)                             # pady= 10 agrega espacio vertical

btn_mostrar = ttk.Button(root, 
                        text = "📇 Mostrar Contactos",
                        command = mostrar_contactos)
btn_mostrar.pack(pady=5)

btn_salir = ttk.Button(root, 
                        text = "🚪 Salir",
                        command = root.destroy)
btn_salir.pack(pady=15)

# Inicar la interfaz
root.mainloop() 
    # Es olbigatorio, 
    # Mantiene la ventana abierta esperando acciones del usuario
    # Es el "ciclo de vida" de la GUI