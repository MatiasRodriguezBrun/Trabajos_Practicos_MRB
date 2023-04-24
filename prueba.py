#!/usr/bin/ env python3

import re 

def empieza_con_p(lista):
    for elemento in lista:
        pattern = r"^P.*\sP.*"
        resultado = re.findall(pattern, elemento)
        return resultado

lista = ["Práctica Python", "Práctica P++", "Práctica Fortran"]  
print(empieza_con_p(lista))
print()
"""
def empieza_con_p(lista):
    return re.findall("^P.*\sP.*", lista)

lista = ["Práctica Python", "Práctica P++", "Práctica Fortran"]  
print(empieza_con_p(lista))
print()
"""
