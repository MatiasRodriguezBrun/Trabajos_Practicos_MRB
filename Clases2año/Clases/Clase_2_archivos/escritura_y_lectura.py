#!/bin/python3
'''
with open ("mi_nombre.txt", "a") as mi_arch:
    mi_arch.write("Mati Brun")

archivo = open("Clases/archivo.txt")
print (archivo)

#read una linea del archivio - me da una lista
line = archivo.readline()
print(line)

#read todo el archivo - me da un string
contenido = archivo.read()
print (contenido)
'''
# Modo (w) o write
archivo_new = open("archivo_new.txt","w")
archivo_new.write("Hola a todos\n")
archivo_new.write("Espero que esten muy bien\n")

# Si el file NO existe: Crea el archivo. 
# Pero SI existe: Sobrescribe un archivo existente ("lo vacia")

# Modo (a) o append
# Si el file NO existe: Crea el archivo. 
# Pero SI existe: El puntero se ubica al final y AGREGA 
archivo_new = open("archivo_new.txt","a")
archivo_new.write("Hola a todos\n")
archivo_new.write("Espero que esten muy bien\n")

archivo_new.close()