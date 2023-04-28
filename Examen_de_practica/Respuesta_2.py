#!/usr/bin/ env python3
import os, glob, re

def sidra(archivo1, archivo2, base_de_datos):
    with open (archivo1, "r") as file1:
        contenido1 = file1.read()
        correos = re.findall("[a-z0-9]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*", contenido1)
        print (correos)
        print()
    with open (archivo2, "r") as file2:
        contenido2 = file2.read()
        correos2 = re.findall("[a-z0-9]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*", contenido2) 
        print (correos2)
        print()
    with open (base_de_datos, "w") as base_de_datos:
        for correo in correos:
            base_de_datos.write(correo)
        for correo in correos2:
            base_de_datos.write(correo)

print(sidra("archivo1.txt", "archivo2.txt", "base_de_datos.txt"))