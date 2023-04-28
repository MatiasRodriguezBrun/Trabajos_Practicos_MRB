#!/bin/python3

# abrir el archivo y escribir, en este caso se agrega al archivo ya existente
with open ("mi_nombre.txt", "a") as mi_arch:
    mi_arch.write("Mati Brun\n")

#lee la primer linea del archivio 
with open ("archivo.txt", "r") as file:
    line = file.readline()
    print(line) # 1. Archivo
print ()

#lee todo el archivo, lo devuelve en forma de lista y separa las lineas mediante \n (saltos de linea)
with open ("archivo.txt", "r") as file:
    line = file.readlines()
    print(line) # ['1. Archivos\n', '\n', 'Python tiene la capacidad de acceder....
print ()

#read todo el archivo - me da un string
with open ("archivo.txt", "r") as file:
    contenido = file.read()
    print (contenido)

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
