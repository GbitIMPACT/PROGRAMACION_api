class Libro:
    def __init__(self, titulo, autor, anho):
        self.titulo = titulo
        self.autor = autor
        self.anho = anho

    def mostrarDatos(self):
        print(f"El libro {self.titulo} con autor {self.autor} se publicó en el año {self.anho}") 