

# SISTEMA DE GESTION DE USUARIOS PARA VOTAR

Sistema_Usuarios=[]


def registro_usuario(nombre_usuario, clave, voto):
   user = [nombre_usuario, clave, voto]
   Sistema_Usuarios.append(user)
   print("\n Voto creado")

def actualizar_voto(nombre_usuario,clave,nuevo_voto):
   for user in Sistema_Usuarios:
      if user[0]==nombre_usuario and user[1]==clave:
         user[2]=nuevo_voto
         print("Su voto ha cambiado")
         break
   else: print("el usuario o la clave son incorrectos")

def cambiar_contraseña(nombre_usuario,clave,nueva_clave):
   for user in Sistema_Usuarios:
      if user[0]==nombre_usuario and user[1]==clave:
         user[1]=nueva_clave
         print("Su voto ha cambiado")
         break
   else: print("El usuario o la clave son incorrectos")

def eliminar_voto(nombre_usuario,clave):
   for user in Sistema_Usuarios:
      if user[0]==nombre_usuario and user[1]==clave:
         Sistema_Usuarios.remove(user)
         print("Eliminado")
         break
   else: print("El usuario o la clave son incorrectos")

def mostrar_resultados():
   print("\033[91m--------------------\nLos resultados son:\n-------------------- \033[0m")
   for user in Sistema_Usuarios:
      print(user[2])




##Menú
while True:
   print("\033[92m________________ \n______MENÚ______\n   \033[0m")
   print("1) Mostrar candidatos ")
   print("2) Agregar voto")
   print("3) Actualizar voto")
   print("4) Eliminar voto")
   print("5) Mostrar resultados")
   print("6) Abandonar menú")
   print("\033[92m________________ \n\033[0m")

   opcion = (input("\033[93mElija una opción: \033[0m"))

   if opcion=="1":
     print("________________")
     print("Los candidatos son: \n")
     print("Erling")
     print("Francisco")
     print("Helmut")
     print("Antonio")

   elif opcion=="2":
    nombre_usuario =input("Escriba su nombre de usuario:")
    clave= input("Escriba una contraseña: ")
    voto=input("Ingrese el nombre del candidato elejido: ")
    registro_usuario(nombre_usuario, clave, voto)

   elif opcion=="3":
    nombre_usuario =input("Escriba su nombre de usuario: ")
    clave= input("Escriba una contraseña: ")
    nuevo_voto=input("Ingrese el nuevo voto: ")
    actualizar_voto(nombre_usuario, clave, nuevo_voto)

   elif opcion=="4":
       nombre_usuario =input("Escriba su nombre de usuario: ")
       clave= input("Escriba una contraseña: ")
       eliminar_voto(nombre_usuario,clave)


   elif opcion== "5":
      mostrar_resultados()

   elif opcion=="6":
       print ("Saliendo")
       break

   else:
       print("Opción invalida")
   
    

   
