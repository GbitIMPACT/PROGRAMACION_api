def votacion():
    nombre = input("\nIngrese su nombre\n")
    edad = int(input("Ingrese su edad"))

    if(edad > 18):
        print(f"Hola {nombre}! si puedes votar")
    else:
        print(f"Hola {nombre}! NO puedes votar")

def cajero():
    saldo = int(input("\nIngrese su saldo\n"))
    
    while saldo > 0:
        retiro = int(input("\nIngrese cuanto va a retirar: \n"))
        if retiro > saldo:
            print("no cuentas con fondos disponibles")
            print(f"saldo restante {saldo}$") 
        else:
            saldo -= retiro
            print(f"saldo restante {saldo}$") 
    
    print("te quedaste sin saldo D:")

def buscarFruta():
    frutas = ["banano", "fresa", "mango", "manzana"]
    nombre = input("\nIngrese el nombre a buscar\n")

    flag = False;
    if(nombre in frutas):
        print("existe")
    else:
        print("no existe")

buscarFruta()