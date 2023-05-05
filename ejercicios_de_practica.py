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

# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la 
# letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
def empieza_con_p(lista):
    lista_nueva = []
    for elemento in lista:
        lista_nueva.append(re.findall(r"^P[^0-9]*\sP[^0-9]*", elemento))
    return lista_nueva

print(empieza_con_p(["Práctica Python", "Práctica P++", "Práctica Fortran"]))



