import sqlite3
from producto import Producto  

class Inventario:
    def __init__(self, db_name="inventario.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS inventarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            unidad INTEGER NOT NULL
        )
        ''')
        self.conn.commit()

    def añadir(self, nombre, precio, unidad):
        self.c.execute("INSERT INTO inventarios (nombre, precio, unidad) VALUES (?, ?, ?)",
                       (nombre, precio, unidad))
        self.conn.commit()
        print("Añadido con éxito")

    def mostrar(self):
        self.c.execute("SELECT * FROM inventarios")
        datos = self.c.fetchall()
        if not datos:
            print("No hay productos en el inventario.")
        for fila in datos:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Precio: {fila[2]}, Unidad: {fila[3]}")

    def buscar(self, id):
        self.c.execute("SELECT * FROM inventarios WHERE id = ?", (id,))
        tabla_resultado = self.c.fetchone()
        return tabla_resultado
        

    def actualizar(self, id, nuevo_nombre, nuevo_precio, nueva_unidad):
        producto = self.buscar(id)
        if producto:
            self.c.execute('''
            UPDATE inventarios
            SET nombre = ?, precio = ?, unidad = ?
            WHERE id = ?
            ''', (nuevo_nombre, nuevo_precio, nueva_unidad, id))
            self.conn.commit()
            print("Producto actualizado con éxito")

    def eliminar(self, id):
        producto = self.buscar(id)
        if producto:
            self.c.execute("DELETE FROM inventarios WHERE id=? ", (id))
            print("El producto fue eliminado")
