#!/usr/bin/python
"""
# Creá una función denominada eneavo que tenga como argumento un número e imprima el resultado de la división de 
#1 por ese número

def eneavo(numero):
    try: 
        print (1/numero)
    except ZeroDivisionError: # excep solo --> contemplamos cualquier tipo de error 
        print ("No se puede dividir por cero")
    except TypeError:
        print ("El", numero, "es un string")
    
eneavo("9")
eneavo(0) 

#Ejercicio 1
# Dado el siguiente bloque de código contestar:

def lista_super():
    lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
    try:
        lista_super + "arroz"
    except:
        print("no puedo agregar arroz")
lista_super()

# ¿Es correcto el uso del try...except? ¿Qué cosa/s le modificarías?
# Falta el tipo de error que estamos esperando y un mensaje claro cuando ocurra ese error 

#Ejercicio 2
# Definir una función que tenga como parámetros una lista de números por un lado y un número por otro y 
# devuelva una lista con la división de cada elemento por el número dado. Por ejemplo, si le paso ([2,4,6,8], 2), 
# debería retornar [1,2,3,4]. Tomar las precauciones necesarias.
def division_de_numeros(lista_de_numeros, numero):
    lista_nueva = []
    try:
        for i in lista_de_numeros:
            lista_nueva.append(i/numero)
    except ZeroDivisionError: 
        print ("No se puede dividir por cero")
    return (lista_nueva)
            
print(division_de_numeros([2,4,6,8], 2))
print(division_de_numeros([2,4,6,8], 0))
"""
#Ejercicio 3
# Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar el número a la lista solo
# si el número es positivo. De lo contrario debería generar un error indicando que el número no es positivo.
def division_de_numeros(lista_de_numeros, numero):
    if numero < 0:
            raise Exception (f"solo se agregan numeros positivos a la lista, y {numero} es negativo")
    else:
         lista_de_numeros.append(numero)
    print (lista_de_numeros)
    
division_de_numeros([2,4,6,8], 2)
division_de_numeros([2,4,6,8], -2)