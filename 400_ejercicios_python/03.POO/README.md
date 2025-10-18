```python
"""
Clase Música: Implementa una clase Musica con atributos como título, 
artista y género, y métodos para reproducir y pausar la música.
"""
#Tkinter es el modulo estandar para crear interfaces graficas
import tkinter as tk
#Pygame es el modulo para que cada boton llame una función dentro de la clase
# Pygame servira para reproducir el audio
import pygame
#filedialog abre un a ventana para seleccionar un archivo
from tkinter import filedialog

class MusicPlayer:
    def __init__(self,root):
        self.root = root                        # sera la ventana Tkinter que se pasa desde fuera
        """ personalizar la ventana """
        self.root.title("🎵 Reproductor de Música") # titulo del reproductor
        self.root.geometry("400x300")                # ancho x alto
        self.root.config(bg="#1e1e1e")             # color de fondo en formato hexadecimal

        """inicializar el sistema de sonido de pygame"""
        pygame.mixer.init()
        #Banderas para saber si hay musica cargada y si esta en pausa
        self.is_paused   = False
        self.file_loaded = False

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
        self.btn_load = tk.Button(root, text="📂 Cargar canción", command=self.load_music, width=20, bg="#3a3a3a", fg="white")
        self.btn_load.pack(pady=5)

        self.btn_play = tk.Button(root, text="▶️ Reproducir", command=self.play_music, width=20, bg="#3a3a3a", fg="white")
        self.btn_play.pack(pady=5)

        self.btn_pause = tk.Button(root, text="⏸️ Pausar", command=self.pause_music, width=20, bg="#3a3a3a", fg="white")
        self.btn_pause.pack(pady=5)

        self.btn_resume = tk.Button(root, text="▶️ Reanudar", command=self.resume_music, width=20, bg="#3a3a3a", fg="white")
        self.btn_resume.pack(pady=5)

        self.btn_stop = tk.Button(root, text="⏹️ Detener", command=self.stop_music, width=20, bg="#3a3a3a", fg="white")
        self.btn_stop.pack(pady=5)

    """--- Metodos funcionales --- """
    # 📂 load_music() -- Abre un cuadro de diálogo para elegir una canción y la carga en memoria.
    def load_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])    # filedialog.askopenfilename() abre el buscador de archivos.
        if file_path:
            pygame.mixer.music.load(file_path)                                           # pygame.mixer.music.load() carga el archivo seleccionado.
            self.file_loaded = True
            self.label.config(text=f"Cargado: {file_path.split('/')[-1]}")               # label.config() actualiza el texto del estado.

    # ▶️ play_music() -- Reproduce la canción si ya está cargada.
    def play_music(self):
        if self.file_loaded:
            pygame.mixer.music.play()
            self.label.config(text="🎶 Reproduciendo música...")
        else:
            self.label.config(text="⚠️ Primero carga una canción.")
    
    # ⏸️ pause_music() -- Pausa la música sin reiniciar la canción.
    def pause_music(self):
        if self.file_loaded:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.label.config(text="⏸️ Música en pausa.")
        else:
            self.label.config(text="⚠️ No hay canción para pausar.")

    # ▶️ resume_music() -- Reanuda la reproducción desde donde se pausó.
    def resume_music(self):
        if self.file_loaded and self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.label.config(text="▶️ Música reanudada.")
        else:
            self.label.config(text="⚠️ No hay música en pausa.")

    # ⏹️ stop_music() -- Detiene la reproducción completamente.
    def stop_music(self):
        if self.file_loaded:
            pygame.mixer.music.stop()
            self.label.config(text="⏹️ Música detenida.")
        else:
            self.label.config(text="⚠️ No hay canción cargada.")

""" -- Ejecutar la aplicacion -- """
#esta es una ventana contenedor del programa, donde estaran los botnoes y textos
root = tk.Tk()
#Crear una ventana principal y pasarla a la clase
app = MusicPlayer(root)
#mantener la ventana abierta, para que no se cierre inmediatamente
root.mainloop()
```