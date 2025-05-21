class Libro:
    def __init__(self,titulo,autor,genero):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero

    def informacion(self):
        print(f"El libro {self.titulo} es de genero {self.genero} y fue escrito por {self.autor}")