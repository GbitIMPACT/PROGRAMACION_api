class Rectangulo():
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcularArea(self):
        return f"El área es: {self.largo * self.ancho}"

    def calcularPerimetro(self):
        return f"El perimetro es: {(self.largo * 2) + (self.ancho * 2)}"