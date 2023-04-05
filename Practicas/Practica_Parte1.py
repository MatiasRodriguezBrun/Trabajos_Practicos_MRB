#!/usr/bin/ env python3

#Ejercicio 1
# Escribir funciones que permitan obtener el anterior y el siguiente de un número.
def siguiente(numero):
    return numero + 1
print(siguiente(10))

def anterior(numero):
    return numero - 1
print(anterior(10))

#Ejercicio 2
# Escribir una función que obtenga el doble de un número.
def doble(numero):
    return numero*2
print (doble(10))

#Ejercicio 3
# Escribir funciones que obtengan el doble del anterior y el doble del siguiente de un número.
def doble_del_anterior(numero):
    return (numero -1)*2
print (doble_del_anterior(3))

def doble_del_siguiente(numero):
    return (numero +1)*2
print (doble_del_siguiente(3))

#Ejercicio 4
# Escribir una función llamada retirar_dinero, que tenga como parámetros el saldo y el monto a retirar y que 
# devuelva cuánto saldo queda luego de la extracción. Si retira más dinero que lo que tiene en el saldo debe 
# devolver 0 (no se puede usar if).
def retirar_dinero(saldo,monto):
    return max (saldo-monto,0)
print (retirar_dinero(30,50))

#Ejercicio 5
# Escribir una función llamada dia_de_la_semana_favorito que tome como parámetro un día de la semana y 
# devuelve True si el día es "Sábado" o False si es cualquier otro (no se puede usar if).
def dia_de_la_semana_favorito(dia):
    return {"Lunes": False, "Martes": False, "Miércoles": False, "Jueves": False, "Viernes": 
    False, "Sábado": True, "Domingo": False}.get(dia, False)
print(dia_de_la_semana_favorito("Lunes"))
print(dia_de_la_semana_favorito("Sábado"))

#Ejercicio 6
# Escribir una función que determine si una longitud de onda de una radio está dentro o fuera del rango de 
# recepción de una antena. La longitud de onda mínima que recibe la antena es 223.0 y la máxima es 586.8 (no se puede usar if).
def rango_de_recepcion(longitud_de_onda):
    return 223.0 <= longitud_de_onda <= 586.8
print(rango_de_recepcion(300))
print(rango_de_recepcion(40))

#Ejercicio 7
# Reescribir la función del punto anterior considerando, además, que la longitud de onda no puede ser 314.5 porque ya está ocupada por otra radio (no se puede usar if).

#Ejercicio 8
# Escribir una función llamada tiene_descuento que tome como parámetro una edad y devuelva True en caso de que la edad sea menor o igual a 12 o mayor o igual a 60. En caso contrario tiene que devolver False (no se puede usar if).

#Ejercicio 9
# En lógica, los operadores lógicos Y y O se conocen como conjunción y disyunción, respectivamente y se los puede visualizar mediante tablas de verdad:
'''
Conjunción:

conjuncion

Disyunción:

disyuncion

Además, existen más operadores lógicos, como es el caso de la disyunción exclusiva (o XOR) que responde a esta tabla de verdad:

disyuncion_exclusiva

Sin embargo, este operador no está presente en muchos lenguajes de programación. Escribir una función xor que tome como parámetro dos booleanos y retorne el booleano correspondiente con la tabla.
'''
#Ejercicio 10
# Escribir una función que reciba un nombre y un apellido y devuelva un saludo de bienvenida para esa persona.

#Ejercicio 11
# Escribir una función que tome como parámetro un string y que, si empieza con la letra "H", nos devuelva la longitud del string.

#Ejercicio 12
# Escribir una función que reciba como parámetro un string y nos diga si el string empieza con "Buenos" o "Buenas".

#Ejercicio 13
# Escribir una función llamada es_multiplo que reciba dos números y diga si el segundo es múltiplo del primero

#Ejercicio 14
# Escribir una función que nos diga si un número es par, impar o cero.

#Ejercicio 15
# Escribir una función que tome como parámetro una frase y nos diga cuántas "a" (o "A") hay en la frase, utilizando for.

#Ejercicio 16
# Escribir una función que tome como valor una cantidad de dinero y nos diga por cuántos meses podemos subsistir con ese dinero, tomando en cuenta que se gastan 60000 pesos por mes.
