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
# Reescribir la función del punto anterior considerando, además, que la longitud de onda no puede ser 314.5
# porque ya está ocupada por otra radio (no se puede usar if).
def rango_de_recepcion(longitud_de_onda):
    return 223.0 <= longitud_de_onda <= 586.8 and (longitud_de_onda!=314.5)
print(rango_de_recepcion(300))
print(rango_de_recepcion(40))
print(rango_de_recepcion(314.5))
longitud = 10
mensaje = "La longitud de onda está dentro del rango de recepción" * rango_de_recepcion(longitud) or "La longitud de onda está fuera del rango de recepción"
print(mensaje)

#Ejercicio 8
# Escribir una función llamada tiene_descuento que tome como parámetro una edad y devuelva True en caso de que la 
# edad sea menor o igual a 12 o mayor o igual a 60. En caso contrario tiene que devolver False (no se puede usar if).
def tiene_descuento(edad):
    return 12>=edad or edad>=60
print(tiene_descuento(8))
print(tiene_descuento(60))
print(tiene_descuento(30))

#Ejercicio 9
    # Escribir una función xor que tome como parámetro dos booleanos y retorne el booleano correspondiente con la tabla.
print ("Ejercicio 9")
def disyuncion_exclusiva(a, b):
    if a == True and b == True: 
        resultado = False
        print (resultado)
    elif a == True and b == False: 
        resultado = True
        print (resultado)
    elif a == False and b == True: 
        resultado = True
        print (resultado)
    elif a == False and b == False: 
        resultado = False
        print (resultado)
disyuncion_exclusiva(True, False)
disyuncion_exclusiva(False, False)
def xor(a, b):
    return (a and not b) or (not a and b)
xor(True, False)
xor(True, True)

#Ejercicio 10
# Escribir una función que reciba un nombre y un apellido y devuelva un saludo de bienvenida para esa persona.
def saludo():
    nombre = input("Dame tu nombre y apellido: ")
    print (f"Hola {nombre}, bienvenido a python")
saludo()

#Ejercicio 11
# Escribir una función que tome como parámetro un string y que, si empieza con la letra "H", nos devuelva la 
# longitud del string.
def longitud_h(palabra):
    longitud = len(palabra)
    if palabra[0]=="H":
        print (f"La longitud del string es de {longitud}")
    else:
        print("La palabra no comienza con h")
longitud_h("Hongo")
longitud_h("Tango")

#Ejercicio 12
# Escribir una función que reciba como parámetro un string y nos diga si el string empieza 
# con "Buenos" o "Buenas".
def buenas_o_buenos(frase):
    if frase.startswith("Buenos"):
        print ("La frase comienza con Buenos")
    elif frase.startswith('Buenas'):
        print ("La frase comienza con Buenas")
    else:
        return None
buenas_o_buenos("Buenos dias")
buenas_o_buenos("Buenas tardes")

def buena(frase):
    if frase[4] == "a":
        print ("La frase comienza con Buenas")
    elif frase[4] == "o":
        print ("La frase comienza con Buenos")
buena("Buenos dias")
buena("Buenas tardes")

#Ejercicio 13
# Escribir una función llamada es_multiplo que reciba dos números y diga si el segundo
# es múltiplo del primero
def es_multiplo(numero1, numero2):
    if numero1%numero2==0:
        print(f"{numero2} es multiplo de {numero1}")
    else:
        print(f"{numero2} NO es multiplo de {numero1}")
es_multiplo(10, 2)

#Ejercicio 14
# Escribir una función que nos diga si un número es par, impar o cero.
def par_impar(numero1):
    if numero1==0:
        print(f"El {numero1} es igual a cero")
    elif numero1 % 2==0:
        print(f"El {numero1} es par")
    else:
        print (f"El {numero1} es impar")
par_impar(4)
par_impar(5)
par_impar(0)

#Ejercicio 15
# Escribir una función que tome como parámetro una frase y nos diga cuántas "a" (o "A") hay en la frase,
# utilizando for.
def contador_de_a(frase):
    contador = 0
    for letra in frase:
        if letra == "a" or letra == "A":
            contador += 1
    print(f"La cantidad de letras a que hay en la frase son {contador}")
contador_de_a("Habia una vez")

#Ejercicio 16
# Escribir una función que tome como valor una cantidad de dinero y nos diga por cuántos meses podemos 
# subsistir con ese dinero, tomando en cuenta que se gastan 60000 pesos por mes.
def finanzas_personales(dinero):
    presupuesto = int(dinero/6000)
    if presupuesto ==1:
        print (f"Con la cant de dinero que se tiene se puede subsistir un mes")
    else:
        print((f"Con la cant de dinero que se tiene se pueden subsistir {presupuesto} meses"))
finanzas_personales(6000)
finanzas_personales(18000)
finanzas_personales(13000)

