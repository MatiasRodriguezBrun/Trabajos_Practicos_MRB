#!/usr/bin/python
import os, sys, glob 

def primeras_lineas(path_a_text, path_resultado, salida):
    # movemos a marzo 
    os.chdir(path_a_text)
    # extraemos los archvos .txt
    textos = glob.glob("*.txt") 
    # leemos las primeras lineas de los archivos txt
    primer_linea = []
    for txt in textos:
        with open (txt, "r") as file:
           primer_linea.append(file.readline())
    # hacemos carpeta de salida
    os.chdir("../../")
    os.mkdir(path_resultado)
    # escribir esas lineas en un archivo nuevo
    os.chdir(path_resultado)
    with open (salida, "a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")

#otra forma
def copiar_la_primer_linea(archivo_salida):
    os.chdir("Marzo")
    txt = glob.glob("*.txt")
    print (txt)
    
    if not os.path.exists("Resultados"):
        os.mkdir("Resultados")
    else:
        print ("No se puede crear porque la carpeta Resultados ya existe")

    for archivo in txt:
        with open (archivo, "r") as file:
            primer_lineas = file.readline()
        os.chdir("Resultados")
        with open (archivo_salida, "a") as salida:
            salida.write(primer_lineas)
        os.chdir("../")

copiar_la_primer_linea("salida.txt")