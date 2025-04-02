class Pelicula:
    def __init__(self,titulo,director,anho):
        self.titulo=titulo
        self.director=director
        self.anho=anho
        self.actors=[]
    
    def add_actor(self,nombre,apellido,rol):      
        self.actors.append({'Rol':rol,'nombre':nombre,'apellido':apellido})
    
    def list_actor(self):
        


