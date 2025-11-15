import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

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

os.chdir(os.path.dirname(__file__)) # Garantiza que busque en la carpeta correcta

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

def editar_contacto():
    nombre = entry_nombre.get().strip()

    if not nombre:
        messagebox.showwarning("⚠️ Error", "❗ Debe ingresar un nombre para editar.")
        return

    if nombre not in agenda:
        messagebox.showerror("❌ Error", "Ese contacto no existe en la agenda.")
        return

    # Crear ventana secundaria (popup)
    win = tk.Toplevel(root)
    win.title(f"✏️ Editar {nombre}")
    win.geometry("300x150")

    ttk.Label(win, text=f"Editar teléfono de\n👤 {nombre}", font=("Segoe UI", 10)).pack(pady=10)

    entry_new_phone = ttk.Entry(win)
    entry_new_phone.insert(0, agenda[nombre])
    entry_new_phone.pack(pady=5)

    def guardar_cambios():
        nuevo = entry_new_phone.get().strip()
        if not nuevo.replace(" ", "").isdigit():
            messagebox.showwarning("⚠️ Error", "📵 Debe ingresar un número válido.")
            return
        agenda[nombre] = nuevo
        messagebox.showinfo("✔️ Editado", f"Nuevo número de {nombre}:\n📞 +{nuevo}")
        win.destroy()

    ttk.Button(win, text="💾 Guardar", style="Accent.TButton", command=guardar_cambios).pack(pady=10)

def eliminar_contacto():
    nombre = entry_nombre.get().strip()

    if not nombre:
        messagebox.showwarning("⚠️ Error", "❗ Debe ingresar un nombre para eliminar.")
        return

    if nombre not in agenda:
        messagebox.showerror("❌ Error", "Ese contacto no existe.")
        return

    confirm = messagebox.askyesno("🗑️ Confirmar eliminación", f"¿Eliminar contacto?\n\n👤 {nombre}\n📞 +{agenda[nombre]}")

    if confirm:
        agenda.pop(nombre)
        messagebox.showinfo("🗑️ Eliminado", f"Se eliminó a:\n👤 {nombre}")
        entry_nombre.delete(0, tk.END)

"""
============================
FUNCIONES DE LA GUI
============================
"""

root = tk.Tk()                   # crea la ventana principal
root.title("📱 Agenda")         # le da un nombre
root.geometry("350x350")        # define su tamaño
root.configure(bg="#F0F4F8")  # color fondo suave

# ===== Estilos internos =====
style = ttk.Style()
style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))
style.configure("Accent.TButton", padding=6, font=("Segoe UI", 10, "bold"), background="#4A90E2")
style.map("Accent.TButton", background=[("active", "#357ABD")])

# ===== Widgets =====
frame = tk.Frame(root, bg="#F0F4F8")
frame.pack(pady=20)

# Entry (campo de texto)
ttk.Label(frame, text="📝 Nombre del contacto:").pack(pady=5)
entry_nombre = ttk.Entry(frame, width=30)
entry_nombre.pack(pady=3)

ttk.Label(frame, text="📞 Teléfono:").pack(pady=5)
entry_telefono = ttk.Entry(frame, width=30)
entry_telefono.pack(pady=3)

# Botones
ttk.Button(root, text="➕ Agregar Contacto", style="Accent.TButton", command=agregar_contacto).pack(pady=10)

ttk.Button(root, text="✏️ Editar", command=editar_contacto).pack(pady=5)

ttk.Button(root, text="🗑️ Eliminar", command=eliminar_contacto).pack(pady=5)

ttk.Button(root, text="📇 Mostrar Contactos", command=mostrar_contactos).pack(pady=5)

ttk.Button(root, text="🚪 Salir", command=root.destroy).pack(pady=15)

# Inicar la interfaz
root.mainloop() 
    # Es olbigatorio, 
    # Mantiene la ventana abierta esperando acciones del usuario
    # Es el "ciclo de vida" de la GUI