#Ejercicio 1
import os, sys
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una 
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
"""
with open("archivo_ej1.txt  ", "r") as miarch:
    contador = 0
    for linea in miarch:
        if not linea.startswith("P"):
                contador += 1
    print(contador, "lineas no comienzan con la letra P")

#Ejercicio 2
# Escribí un programa que lea un archivo e imprima las primeras n líneas.
# range (a(inicio),b(fin),c(paso)) --> por defecto arranca en 0 y el paso es uno
# (para aclarar el paso es necesario poner el inicio) En caso de querer que vaya para atras (0,4,-1)
def read_n_lines(n, archivo):
    with open(archivo, "r") as miarch:
        for linea in range(n):
            print (miarch.readline())

read_n_lines(3, "archivo_ej1.txt")
"""
#Ejercicio 3
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista 
# y luego imprima las n últimas.
def ej3(archivo, n):
    with open (archivo, "r") as miarch:
        for i in miarch:
            lista_de_lineas = miarch.readlines()
        for i in range ((len(miarch))-n), len(miarch):
            print(miarch[i])
            
    return lista_de_lineas
print(ej3("archivo_ej1.txt",3))

#Ejercicio 4
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

#Ejercicio 5
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

#Ejercicio 6
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

#Ejercicio 7
# Escribí un programa que lea un archivo e identifique la palabra más larga, la cual
# debe imprimir y decir cuantos caracteres tiene.
# split() --> por defecto separa el string por espacios en blanco. Ej: "Clase 5 de abril" --> ["CLase","5","de","Abril"]

#Ejercicio 8
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

#Ejercicio 9
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra
# en cuestión con respecto a la cantidad total de palabras.

#Ejercicio 10
# Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo
# dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.