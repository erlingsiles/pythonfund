from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []
    
    def añadir(self, nombre, precio, unidad):
        producto = Producto(nombre, precio, unidad)
        self.productos.append(producto)
        print("Añadido con éxito")

    def mostrar(self):
        for producto in self.productos:
            print(f"Nombre, {producto.nombre}, Precio, {producto.precio}, Unidad, {producto.unidad}")
    
    def buscar(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        else: print("No se encuentra el producto")

    def eliminar(self, nombre):
        producto = self.buscar(nombre)
        if producto:
            self.productos.remove(producto)
            print("El producto fue eliminado")

    def actualizar(self, nombre, nuevo_nombre, nuevo_precio, nueva_unidad):
        producto = self.buscar(nombre)
        if producto:
            producto.nombre = nuevo_nombre
            producto.precio = nuevo_precio
            producto.unidad = nueva_unidad
            print("Productos actualizados")
            