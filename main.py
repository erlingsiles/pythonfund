from inventario import Inventario

inventario_articulo = Inventario()

while True:
    print("1:Agregar: ")
    print("2:Mostrar: ")
    print("3:Buscar: ")
    print("4:Actualizar: ")
    print("5:Eliminar: ")
    print("6:Salir: ")


    opcion = input("Elija Opcion")
    if opcion == "6":
        break

    if opcion == "1":
        nombre = input("Nombre")
        precio = float(input("precio"))
        unidad = int(input("Unidad"))
        inventario_articulo.añadir(nombre, precio, unidad)


    if opcion == "2":
        inventario_articulo.mostrar()
    
    if opcion in ["3","4","5"]:
        nombre = input("Ingrese el nombre")
        if opcion == "3":
            producto = inventario_articulo.buscar(nombre)
            if producto:
                print(f"Nombre, {producto.nombre}, Precio, {producto.precio}, Unidad, {producto.unidad}")

        elif opcion == "4":
            nuevo_nombre = input("Ingrese nuevo nombre")
            nuevo_precio = float(input("Ingrese nuevo precio"))
            nueva_unidad = int(input("Ingrese nuevas unidades"))
        
        elif opcion == "5":
            inventario_articulo.eliminar(nombre)

        
            