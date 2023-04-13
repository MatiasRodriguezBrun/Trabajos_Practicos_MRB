#!/usr/bin/ env python3

# EXPRESIONES REGULARES

#Tarea de expresiones regulares
#Desafio I: r "\d {4,}" --> obtener al menos 4 digitos 
#Desafio II:  "[a-z]{3,6}" --> obtener entre 3 y 6 letras minúsculas
#Desafio III: "ab*" --> obtener todas las apariciones de ab en un string

import re

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
# Busca la PRIMER coincidencia del texto en cualquier parte del texto
print(re.search(patron, texto))
print (texto[22:26])
# La diferencia es que match solo busca la coincidencia al principio del texto
print (re.match(patron, texto))

# Findall me muestra TODAS las coincidencias en una LISTA
print (re.findall(patron, texto))
print (len(re.findall(patron, texto))) #aca quiero saber la cantidad de coincidencias

# Group --> agrupa el string del patron de la busqueda que hice
print (re.search(patron, texto).group())

# El split me permite separar un string usando un caracter
print (re.split(patron, texto))

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "ipsum(.*)sit" #--> todo lo que esta entre ipsum y sit
print (re.search(patron, texto), "\n")
print (re.search(patron, texto).group())
print (re.search(patron, texto).group(0))
#ipsum dolor sit
# El group NO incluye los caracteres que yo busque
print (re.search(patron, texto).group(1))
#dolor
# La función sub permite reemplazar todos las ocurrencias del patrón por otro patrón en un String.
print(re.sub(patron, "###", texto))