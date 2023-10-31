"""
Crea una clase Producto con atributos nombre, precio, y cantidad y
 un método mostrar_info que imprima la información del producto.
Crea una clase Tienda que tenga un atributo productos que sea una lista de instancias de Producto. La clase Tienda debe tener un método agregar_producto para añadir un producto a la lista y un método mostrar_productos que imprima la información de todos los productos en la tienda.
Crea instancias de Producto y Tienda y usa sus métodos para agregar productos a 
la tienda y mostrarlos.
"""



class Producto:
    def __init__(self, nombre, precio, cantidad) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self) -> None:
        print(f"Producto: {self.nombre}\tPrecio: {self.precio}\tCantidad:{self.cantidad}")


class Tienda:
    def __init__(self) -> None:
        self.productos = []
    
    def agregar_producto(self, nuevo_producto: Producto):
        self.productos.append(nuevo_producto)

    def mostrar_productos(self):
        print("Productos: ")
        for producto in self.productos:
            producto.mostrar_info()

# Crear los productos
producto1 = Producto("Manzanas", 10, 20)
producto2 = Producto("Galletas", 4.5, 50)

# Creamos la tienda
tienda = Tienda()
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

tienda.mostrar_productos()