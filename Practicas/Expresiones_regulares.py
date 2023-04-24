#!/usr/bin/ env python3

import re 

#Ejercicio 1
# Escribí un programa que verifique si un string tiene al menos un carácter permitido.
# Estos caracteres son a-z, A-Z y 0-9.
def caracter_permitido(string):
    return bool(re.search("[a-zA-Z0-9.]", string))

print ("El string ", "ABSDSFHSKLasssssaOAF1223", "tiene caracteres permitidos?")
print (caracter_permitido("ABSDSFHSKLasssssaOAF1223"))
print ("El string ", "$%#", "tiene caracteres permitidos?")
print (caracter_permitido("$%#"))
print()

#Ejercicio 2
# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. 
# Estos caracteres son a-z, A-Z y 0-9.

def todos_los_carac_permitidos(string):
    return not bool(re.search("\W", string))

print ("En el string ", "ABSDSFHSKLasssssaOAF1223", "todos los caracteres estan permitidos?")
print (todos_los_carac_permitidos("ABSDSFHSKLasssssaOAF1223"))
print ("En el string ", "aaaaaaaa$#$&aa00As#", "todos los caracteres estan permitidos?")
print (todos_los_carac_permitidos("aaaaaaaa$#$&aa00As#"))
print()

#Ejercicio 3
# Creá un programa que verifique las siguientes condiciones:
#si un string dado tiene una h seguida de ninguna o más e.

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
print()
# Ejercicio 4
# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado
# (el string no debe contener espacios).
def palabra_unida_con_guion(string):
    pattern = ("[a-z]+_[a-z]+")
    if re.search(pattern, string) is not None:
        return "Patron encontrado"
    else:
        return "Patron NO encontrado"

print(palabra_unida_con_guion("hola_mi_nombre"))
print(palabra_unida_con_guion("hola mi nombre"))
print()

#Ejercicio 5
# Escribí un programa que diga si un string empieza con un número específico.
def empieza_con_numero(string):
    return bool (re.search("^[5]", string))
print("El string comienza con el numero especifico?")
print(empieza_con_numero("54321"))
print("El string comienza con el numero especifico?")
print(empieza_con_numero("12345"))
print()

#Ejercicio 6
# Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
def frase_ej6(string, frase):
    patron = frase
    return bool (re.search(patron, string))

print(frase_ej6("Hola como andan", "Hola como"))
print(frase_ej6("Hola como andan", "Hi"))
print()
#Ejercicio 7
# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios
# y números.
def ej_7(string):
    return bool (re.search(r"^[a-zA-Z0-9\s]+$", string)) #es lo mismo si pongo la r o no? xq yo lo corro de las
    #maneras y es lo mismo

print(ej_7("Las gallinas son asi, 77")) #False
print(ej_7("Las gallinas son asi 77")) #True
print(ej_7("L#as gallinas son asi 77")) #False
print(ej_7("Las gallinas son asi")) #True
print(ej_7("%%$#..Las gallinas son asi")) #False
print()
#Ejercicio 8
# Escribí un programa que separe y devuelva los caracteres númericos de un string.
def extraer_numeros(string):
    resultado =  re.split("\D+", string)
    for elemento in resultado:
        print (elemento)

print (extraer_numeros("La bombonera se creo en 1940. Este año(2023), se propuso un proyecto de cambio en 5 años"))
print (extraer_numeros("4323944"))
print()
#Ejercicio 9
# Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
def entre_guiones(string):
    return re.findall(r"-(.*?)-", string)
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(entre_guiones(string))
print()
#Ejercicio 10
# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings
#  están delimitadas por los caracteres @ o &.
def posicion(string):
    pattern = "[@&](.*?)[@&]"
    # Busca todas las apariciones del patrón dentro del string, como findall pero devuelve un iterador 
    # que podemos utilizar para obtener información sobre cada aparición encontrada
    resultados = re.finditer(pattern, string)
    for resultado in resultados:
        substring = resultado.group(1)
        inicio = resultado.start()
        fin = resultado.end() - 1
        print(f"Substring: {substring}, Posición inicial: {inicio}, Posición final: {fin}")

print(posicion("La libertad @esta dada@ por &cuestiones@ que van mas alla de todo"))
print()
#Ejercicio 11
# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la 
# letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
def empieza_con_p(lista):
    for elemento in lista:
        pattern = r"^P.*\sP.*"
        resultado = re.findall(pattern, elemento)
        return resultado

lista = ["Práctica Python", "Práctica P++", "Práctica Fortran"]  
print(empieza_con_p(lista)) #solo me muestra ['Práctica Python'] 
print()
#Ejercicio 12
# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos
# por la barra vertical (|).
def reemplazar(string):
    pattern = "[\s_:]+"
    return re.sub(pattern, "|" , string)

print(reemplazar("Los ingredientes son: agua_leche_harina"))
print()
#Ejercicio 13
# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
def reemplazar_alfanumericos(string):
    pattern = r"\W{2}?" # en este caso solo me lo reemplaza si encuentra dos, si encuentra menos no lo hace.
    # Ademas me di cuenta que solo lo reemplaza si estan juntos porque el punto(.) tamebien es un caracter NO alfanumerico
    return re.sub(pattern, "__" , string, count=2)

print(reemplazar_alfanumericos("matias@mail.com"))#no me reemplaza nada ni el @ ni el punto
print(reemplazar_alfanumericos("matias@mail@.com"))#aca si me reemplaza porque estan juntos (matias@mail__com)
print(reemplazar_alfanumericos("matias###gm$ail.com"))
print(reemplazar_alfanumericos("!!matias###gm$ail.com"))#no solo me reemplaza las dos primera (!!) sino que tambien ##
print()

#Ejercicio 14
# Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
def reemplazar_espacios(string):
    pattern = "\s"
    return re.sub(pattern, ";", string)

print(reemplazar_espacios("Las gallinas son      asi, es lo   que hay"))
print()
#Ejercicio 15
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.
def validar_mail(mail):
    return bool (re.search("^[a-z0-9]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*$", mail))

print(validar_mail("matias@gmail.com")) #True
print(validar_mail("matias.brun@gmail.com")) #True
print(validar_mail("matias%%brun@gmail.com")) #False
print(validar_mail("@@matias%%brun@gmail.com")) #False
