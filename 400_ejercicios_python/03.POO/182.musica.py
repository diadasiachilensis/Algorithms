"""
Clase Música: Implementa una clase Musica con atributos como título, 
artista y género, y métodos para reproducir y pausar la música.
"""
#Tkinter es el modulo estandar para crear interfaces graficas
import tkinter as tk

class MusicPlayer:
    def __init__(self,root):
        self.root = root                        # sera la ventana Tkinter que se pasa desde fuera
        """ personalizar la ventana """
        self.root.title("🎵 Reproductor de Música") # titulo del reproductor
        self.root.geometry("400x300")                # ancho x alto
        self.root.config(bg="#1e1e1e")             # color de fondo en formato hexadecimal

        """Para mostrar mensajes"""
        self.label = tk.Label(                  # Label crea un texto visible
            root,
            text = "No hay cancion cargada",
            fg   = "white",
            bg   = "#1e1e1e",
            font = ("Arial", 12) 
        )
        self.label.pack(pady=20)               # .pack() lo coloca en la ventana con un margen vertical (pady=20).

        """Botones principales"""
        self.btn_load = tk.Button(
            root,
            text  = "📂 Cargar canción",
            width = 20,
            bg    = "#3a3a3a",
            fg    = "white"
        )
        self.btn_load.pack(pady=5)

        self.btn_play = tk.Button(
            root, 
        )

""" -- Ejecutar la aplicacion -- """
#esta es una ventana contenedor del programa, donde estaran los botnoes y textos
root = tk.Tk()
#Crear una ventana principal y pasarla a la clase
app = MusicPlayer(root)

#mantener la ventana abierta, para que no se cierre inmediatamente
root.mainloop()
