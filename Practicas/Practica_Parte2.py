#!/usr/bin/ env python3
#Ejercicio 1
# Definir un procedimiento que tome como parámetro una lista, verifique si tiene el elemento "control"
# y le agregue el string "revisado" y le quite el elemento "control".
procedimiento = ["venta", "confirmacion", "control", "armado de pedido"]
def lista(procedimiento):
    if "control" in procedimiento:
        procedimiento.remove("control")
        procedimiento.append("revisado")
        return procedimiento
print(lista(procedimiento))

#Ejercicio 2
# Definir un procedimiento que tome una lista como parámetro y elimine el primer elemento de la lista.
# Hacer las verificaciones que sean necesarias.
def eliminar_1er_elemento(lista):
    lista.pop(0)
    return lista
lista = [10,20,30,43]
print(eliminar_1er_elemento(lista))

#Ejercicio 3
# Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista.
def posición(lista,elemento):
    return lista.index(elemento)
print(posición(lista, 30))
print() 

#Ejercicio 4
# Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar el 
# elemento de una lista y agregarlo a la otra. Realizar dos versiones del ejercicio, usando un método 
# distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?
def ej_4(lista1,lista2,elemento):
    lista1.remove(elemento)
    lista2.append(elemento)
    print(lista1)
    print(lista2) 
lista1 = [1,2,3,4]
lista2 = [5,6,7]
ej_4(lista1, lista2, 3)
"El codigo corre pero si lo quiero hacer con return se me complica porque solo me retorna una lista"

def ej_4b(lista1,lista2,elemento):
    posicion = lista.index(elemento)
    lista.pop(posicion)
    lista2.append(elemento)
    print(lista1)
    print(lista2) 
lista1 = [1,2,3,4]
lista2 = [5,6,7]
ej_4(lista1, lista2, 3)
"Este procedimiento tiene dos problemas; 1)Modifica las listas originales, 2)si el elemento que se quiere borrar"
"aparece mas de una vez solo lo borra una unica vez"
#Ejercicio 5
# Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores 
# booleanos que indique si cada elemento es par o impar. Por ejemplo, para la lista [2, 45, 108, 12, 7], 
# la función debería retornar [True, False, True, True, False]. Utilizar la función realizada en la práctica anterior.
def par_impar(lista_enteros):
    lista_nueva = []
    for numero in lista_enteros:
        if numero %2 == 0:
            numero = True
            lista_nueva.append(numero)
        else:
            numero = False
            lista_nueva.append(numero)
    return lista_nueva
lista_enteros = [2, 45, 108, 12, 7]
print(par_impar(lista_enteros))

#Ejercicio 6
# Escribir una función que lea un string y devuelva un diccionario con la cantidad de apariciones de cada carácter
#  en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua",
#  el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
def caracteres(palabra):
    dic = {}
    for caracter in palabra:
        caracter = caracter.lower()
        if caracter in dic:
            dic[caracter] += 1
        else:
            dic[caracter] = 1
    return dic
print(caracteres("Agua"))

#Ejercicio 7
# Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el
# valor 0.
import string

def caracteres1(palabra1):
    diccionario = {}
    for caracter in palabra1:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    for letra in string.ascii_lowercase:
        if letra not in diccionario:
            diccionario[letra] = 0
    return diccionario
print(caracteres1("Agua"))

#Ejercicio 8
# Definir una función que dada una palabra, nos diga si el palíndromo o no.
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    # Verificar si la palabra es igual al revés
    if palabra == palabra[::-1]:
        return palabra + " es palíndromo"
    else:
        return palabra + " no es palíndromo"
print(es_palindromo("Ana"))
print(es_palindromo("Palabra"))

#Ejercicio 9
# Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.
lista_de_números = [1, 2, 3, 4, 5]
def productoria(lista_de_números):
    resultado = 1
    for numero in lista_de_números:
        resultado *= numero
    return resultado
print(productoria(lista_de_números))

#Ejercicio 10
# Creá un programa para gestionar datos de los socios de un club, el cual permita:
'''
Cargar la información de los socios en un diccionario, al cual poder acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día

Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día

Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

Informar la cantidad de socios que tiene el club.

Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

Imprimir el listado de socios completos.

Definir las funciones y/o procedimientos que creas necesarios.
'''

