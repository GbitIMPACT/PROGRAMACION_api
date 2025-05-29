from Rectangulo import Rectangulo
from Estudiante import Estudiante
from Libro import Libro

r1 = Rectangulo(5, 4)
print(r1.calcularArea())
print(r1.calcularPerimetro())


e1 = Estudiante("Mene", 18, "ADSO")
e1.saludar()

l1 = Libro("50 sombras mas negras", "mene", 2020)
l1.mostrarDatos()