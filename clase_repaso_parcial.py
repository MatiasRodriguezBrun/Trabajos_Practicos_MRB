#!/usr/bin/env python3
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