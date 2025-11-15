import tkinter as tk
from tkinter import messagebox

from contact_manager import {
    agenda, add_contact, del_contact, edit_contact, search_contact
}

"""
============================
FUNCIONES DE LA GUI
============================
"""
root = tk.TK()                  # crea la ventana principal
root.title("📱 Agenda")         # le da un nombre
root.geometry("320x300")        # define su tamaño

# Etiquetas 
label_nombre = tk.Label(root, text="📝 Nombre del contacto:")   # Label = texto descriptivo
label_nombre.pack()                                             # .pack() lo acomoda automaticamente

# Entry (campo de texto)
entry_nombre = tk.Entry(root)
entry_nombre.pack()              # Lugar donde el usuario escribe

label_telefono = tk.Label(root, text = "📞 Teléfono:")
label_telefono.pack()

entry_telefono = tk.Entry(root)
entry_telefono.pack()

# Botones
btn_agregar = tk.Button(root,
                        text = "➕ Agregar Contacto",  # Button crea un boton
                        command = agregar_contacto)     # command = le indica que funcion ejecutar cuando lo presionas
btn_agregar.pack(pady = 10)                             # pady= 10 agrega espacio vertical

btn_mostrar = tk.Button(root, 
                        text = "📇 Mostrar Contactos",
                        command = mostrar_contactos)
btn_mostrar.pack()

btn_salir = tk.Button(root, 
                        text = "🚪 Salir",
                        command = root.destroy)
btn_salir.pack(pady=15)

# Inicar la interfaz
root.mainloop() 
    # Es olbigatorio, 
    # Mantiene la ventana abierta esperando acciones del usuario
    # Es el "ciclo de vida" de la GUI