#!/usr/bin/ env python3
import re, glob, os

# Expresiones regulares
"""
# 1 - encontrar los sustantivos propios
def encontrar_sus_propios(string):
    return re.findall(r"[A-Z]\w+", string) 
                             #[a-z] no incluye las letras con tilde

print(encontrar_sus_propios("María y Andrés tienen 3 hijos, Juan, 16 años, Marcela de 10 y Daniel de 5"))

# 2 - obtener las lista de personas con sangre tipo O+
# Matias Brun: 0+ 
def sangre_tipo_o_positivo(archivo):
    with open (archivo, "r") as file:
        file = file.read()
        resultado = []
        for item in re.findall("(\w+\s\w+)(:\sO+)", file): # dos grupos (nombre y apellido) y (tipo de sangre)
            resultado.append(item[0]) #aca puede ser 0 o 1 que son los grupos, pongo 0 para obtener LOS NOMBRES DE LOS
                                  # que tienen sangre tipo O+ 
        return resultado
print(sangre_tipo_o_positivo("tipo_de_sangre.txt"))
"""

"""
#Ejercicio 10
# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings
#  están delimitadas por los caracteres @ o &.

def obtener_substrings(string):
    return re.findall(r"[@|&](.*)[@|&]", string)

print(obtener_substrings("matias@gmail@com"))
print(obtener_substrings("matias&gmail&com")) 
"""
"""
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una 
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P")

def ej1(archivo):
    with open(archivo, "r") as miarch:
        texto = miarch.read()
        empieza_con_p = re.findall(r"[P]", texto)
        print ("Sabemos que", len(empieza_con_p), "lineas empiezan con P")

    with open (archivo, "r") as miarch2:
        leido_en_lista = miarch2.readlines()
        print ("Sabemos que el archivo total tiene", len(leido_en_lista), "lineas")

        lineas_no_empiezan_con_p = len(leido_en_lista) - len(empieza_con_p)
        print (f"Por lo tanto {lineas_no_empiezan_con_p} lineas no empiezan con la letra P")

ej1("tipo_de_sangre.txt")
"""
# a) Obtener la lista de subsecuencia delimitadas por X e Y que incluyan las subsecuencia "ab". 
# Por ej para XbaaaYjXababYqXbabbbbaaYqXffeeY, hay que devolver ["abab, "babbbaa"]
def obtener_subsecuencia(string):
    return re.findall(r"ag([^0-9]*)cta", string)

print(obtener_subsecuencia("aabocaggaaactazudlggaasag24gra1ndecta"))
