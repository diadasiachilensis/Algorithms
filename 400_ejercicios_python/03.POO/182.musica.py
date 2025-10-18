"""
Clase Música: Implementa una clase Musica con atributos como título, 
artista y género, y métodos para reproducir y pausar la música.
"""
class Musica:
    def __init__(self):
        self.albums = []
    
    def add_album(self,title,artist,genre):
        self.albums.append({
            'artist' : artist,
            'title'  : title,
            'genre'  : genre
        })
    
    def play(self,name):
        for music in self.albums:
            if music['title'].lower() == name.lower():
                