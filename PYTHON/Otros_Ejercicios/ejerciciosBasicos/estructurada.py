from datetime import date, datetime, timedelta

print ("hola mundo")

# manejo de variables}

nombre = "wilson"
edad = 12
estatura = 1.75
print(f"{nombre} tiene {edad} años y mide {estatura} metros.")

# manejo de tipos 

edad_str = "20"
edad_int = int (edad_str)
print(edad_int+5)



# manejo de fechas
fecha_hoy = date.today()
fecha_hora = datetime.now()
cumpleaños = date(1990,4,15)
mañana = date.today() + timedelta(days=1)
dias_trans = (fecha_hoy - date (2025,1,1)).days
print (cumpleaños)
 
 # manejo de boolenas 
es_mayor_de_edad = True 
tiene_licnecia = False 

if (es_mayor_de_edad and tiene_licnecia):

    print("puede manejar ")

else:
    print("no puede conducir")

# manejo de rangos 

nota = 85 
if nota >= 90:
    print("exelente")
elif nota >= 70:
    print("bien")
else: 
    print("nota mala")

#simulacion de casos 
opccion = 0 
if opccion ==1:
    print("opccion1")
elif opccion == 2:
    print("opccion 2")
else: 
    print("error")

# simulacion de las casos 
def opcciona_1():
    return "opccion 1"
def opccion_2():
    return "opccion 2"
swich = {1: opcciona_1, 2: opccion_2}

resultado = swich.get (2, lambda: "opccion no valida")()
print(resultado) 

#bucles (for y while)

for i in range(1,6):
    print(i)

#bucle while tradicional 
contador = 3
while contador > 0 :
    print (contador)
    contador -=1 

#bucle do while 

while True: 
    numero = int(input("ingrese un numero mayor que 0: "))
    if numero > 0:
        break 


# bucle tipo forech con lista y diccionario 
animales = ["gato", "perro", "conejo"]
for animal in animales: 
    print(animal)
persona = {"persona": "wilson", "edad": 30}
for clave, valor in persona.items():
    print(f"{clave} and {valor}")
