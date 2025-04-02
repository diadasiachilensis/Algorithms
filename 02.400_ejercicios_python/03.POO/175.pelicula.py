class Pelicula:
    def __init__(self, titulo, director, anho):
        self.titulo = titulo
        self.director = director
        self.anho = anho
        self.actors = []
    
    def add_actor(self, nombre, apellido, papel):      
        self.actors.append({'Rol': papel, 'nombre': nombre, 'apellido': apellido})
    
    def list_actor(self):
        print(f"Reparto de la película '{self.titulo}' ({self.anho}):")
        for actor in self.actors:
            nombre_completo = f"{actor['nombre']} {actor['apellido']}"
            print(f"- {nombre_completo} como {actor['Rol']}")

# Crear instancia de la película Blade Runner (1982)
pelicula = Pelicula("Blade Runner", "Ridley Scott", 1982)

# Agregar actores del reparto
pelicula.add_actor("Harrison", "Ford", "Rick Deckard")
pelicula.add_actor("Rutger", "Hauer", "Roy Batty")
pelicula.add_actor("Sean", "Young", "Rachael")
pelicula.add_actor("Edward", "James Olmos", "Gaff")
pelicula.add_actor("Daryl", "Hannah", "Pris")

# Mostrar el reparto
pelicula.list_actor()