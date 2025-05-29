class Producto:
    def __init__(self, identificador, nombre, descripcion, precio, cantidad):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return (f"ID: {self.identificador} | Nombre: {self.nombre} | "
                f"Descripción: {self.descripcion} | Precio: ${self.precio:.2f} | "
                f"Cantidad: {self.cantidad}")

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.identificador in self.productos:
            print(f"Error: Ya existe un producto con ID {producto.identificador}")
        else:
            self.productos[producto.identificador] = producto
            print(f"Producto {producto.nombre} agregado correctamente.")

    def eliminar_producto(self, identificador):
        if identificador in self.productos:
            eliminado = self.productos.pop(identificador)
            print(f"Producto {eliminado.nombre} eliminado.")
        else:
            print("No se encontró el producto con ese ID.")

    def actualizar_producto(self, identificador, nombre=None, descripcion=None, precio=None, cantidad=None):
        if identificador in self.productos:
            producto = self.productos[identificador]
            if nombre:
                producto.nombre = nombre
            if descripcion:
                producto.descripcion = descripcion
            if precio is not None:
                producto.precio = precio
            if cantidad is not None:
                producto.cantidad = cantidad
            print(f"Producto {identificador} actualizado.")
        else:
            print("No se encontró el producto con ese ID.")

    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def filtrar_por_id(self, identificador):
        producto = self.productos.get(identificador)
        if producto:
            print(producto)
        else:
            print("No se encontró el producto con ese ID.")

    def filtrar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Listar todos los productos")
        print("5. Filtrar por identificador")
        print("6. Filtrar por nombre")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_ = input("ID producto: ")
                nombre = input("Nombre: ")
                descripcion = input("Descripción: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad disponible: "))
                nuevo_producto = Producto(id_, nombre, descripcion, precio, cantidad)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Precio y cantidad deben ser numéricos.")

        elif opcion == "2":
            id_ = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_)

        elif opcion == "3":
            id_ = input("ID del producto a actualizar: ")
            print("Dejar en blanco para no cambiar un campo.")
            nombre = input("Nuevo nombre: ").strip()
            descripcion = input("Nueva descripción: ").strip()
            precio_str = input("Nuevo precio: ").strip()
            cantidad_str = input("Nueva cantidad: ").strip()

            nombre = nombre if nombre != "" else None
            descripcion = descripcion if descripcion != "" else None
            precio = float(precio_str) if precio_str else None
            cantidad = int(cantidad_str) if cantidad_str else None

            inventario.actualizar_producto(id_, nombre, descripcion, precio, cantidad)

        elif opcion == "4":
            inventario.listar_productos()

        elif opcion == "5":
            id_ = input("ID para filtrar: ")
            inventario.filtrar_por_id(id_)

        elif opcion == "6":
            nombre = input("Nombre para filtrar: ")
            inventario.filtrar_por_nombre(nombre)

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente otra vez.")

if __name__ == "__main__":
    menu()