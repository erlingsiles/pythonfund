#fich_sal = open("datos/datos.txt","w")

#fich_sal = open("datos/datos.txt",'r')
#for linea in fich_sal:
#    print (linea)

#fich_sal = open("datos/datos.txt","a")
#fich_sal.write("11")
#fich_sal.close()

with open("datos/datos.txt","a") as file:
    file.write("12")
