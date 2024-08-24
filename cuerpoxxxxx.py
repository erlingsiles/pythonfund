from cuerpoxxxxx import Voto

class votacion:
    def __init__(self):
        self.votar=[]
    
    def añadir_voto(self, usuario, clave, voto):
        votos= Voto(usuario, clave, voto)
        self.votar.append(votos)
        print("\n Voto creado")
    
    def mostrar_Voto(self):
        print("\033[91m--------------------\nLos resultados son:\n-------------------- \033[0m")
        for votos in self.votar:
            print(f" {votos.voto}")
        else: print("No hay Votos")

    def cambiar_contraseña(self, usuario, clave, nueva clave):
        
