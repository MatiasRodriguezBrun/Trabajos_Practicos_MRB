#!/usr/bin/ env python3

import re 
#Ejercicio 1
# Escribí un programa que verifique si un string tiene al menos un carácter permitido.
# Estos caracteres son a-z, A-Z y 0-9.
"""
def caracter_permitido(string):
    return bool(re.search("[a-zA-Z0-9.]", string))

print ("El string ", "ABSDSFHSKLasssssaOAF1223", "tiene caracteres permitidos?")
print (caracter_permitido("ABSDSFHSKLasssssaOAF1223"))
print ("El string ", "$%#", "tiene caracteres permitidos?")
print (caracter_permitido("$%#"))
print()
"""
#Ejercicio 2
# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. 
# Estos caracteres son a-z, A-Z y 0-9.
"""
def todos_los_carac_permitidos(string):
    return not bool(re.search("\W", string))

print ("En el string ", "ABSDSFHSKLasssssaOAF1223", "todos los caracteres estan permitidos?")
print (todos_los_carac_permitidos("ABSDSFHSKLasssssaOAF1223"))
print ("En el string ", "aaaaaaaa$#$&aa00As#", "todos los caracteres estan permitidos?")
print (todos_los_carac_permitidos("aaaaaaaa$#$&aa00As#"))
print()
"""
#Ejercicio 3
# Creá un programa que verifique las siguientes condiciones:
#si un string dado tiene una h seguida de ninguna o más e.
"""
def h_seguida_de_e(string):
    return bool(re.search("he*", string))
print (h_seguida_de_e("heeeeeeee"))
print (h_seguida_de_e("he"))
print (h_seguida_de_e("h"))
print (h_seguida_de_e("hehe"))
#si un string dado tiene una h seguida de una o más e.
def h_seguida_de_e(string):
    return bool(re.search("he+", string))
#si un string dado tiene una h seguida de cero o una e.
def h_seguida_de_e(string):
    return bool(re.search("he?", string))
#si un string dado tiene una h seguida de dos o tres e.
def h_seguida_de_e(string):
    return bool(re.search("he{2,3}", string))
"""
"""
# Ejercicio 4
# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado
# (el string no debe contener espacios).
def palabra_unida_con_guion(string):
    pattern = "^[a-z]+_[a-z]$"
    if re.search(pattern, string) is not None:
        return "Patron encontrado"
    else:
        return "Patron NO encontrado"

print (palabra_unida_con_guion("hola_mi_nombre_esmatias_yme_gusta_el futbol"))
"""
#Ejercicio 5
# Escribí un programa que diga si un string empieza con un número específico.
#def empieza_con_numero(string):


#Ejercicio 6
# Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
def frase_ej6(string, frase):
    patron = frase
    return bool (re.search(patron, string))

print(frase_ej6("Hola como andan", "Hola como"))
print(frase_ej6("Hola como andan", "Hi"))

#Ejercicio 7
# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios
# y números.


#Ejercicio 8
# Escribí un programa que separe y devuelva los caracteres númericos de un string.
#def extraer_numeros(string):



#Ejercicio 9
# Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
def entre_guinies(string):
    return re.findall(r"-(.*?)-", string)
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(entre_guinies(string))

#Ejercicio 10
# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings
#  están delimitadas por los caracteres @ o &.

#Ejercicio 11
# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la 
# letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
''' 
def empieza_con_p(lista):
    for elemento in lista:
        resultado = re.match(pattern, string)

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]  
'''  
#Ejercicio 12
# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos
# por la barra vertical (|).

#Ejercicio 13
# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

#Ejercicio 14
# Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

#Ejercicio 15
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.
