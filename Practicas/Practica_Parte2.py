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
    # Compara la palabra original con su versión invertida utilizando la técnica de "slicing" de
    # cadenas de caracteres ([::-1]).
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
# Creá un programa para gestionar datos de los socios de un club:

socios = {1:{"nombre_y_apellido":"Florencia Ocampo","fecha_de_ingreso":"14092001", "cuota_al_dia": True},
2:{"nombre_y_apellido":"David Estévez","fecha_de_ingreso":"14092001", "cuota_al_dia": True},
3:{"nombre_y_apellido":"Sofía Cáceres","fecha_de_ingreso":"14092001", "cuota_al_dia": True}}

def agregrar_socio(numero, nombre_y_apellido, fecha_de_ingreso, cuota_al_dia):
    socios[numero] = {"nombre_y_apellido":nombre_y_apellido, "fecha_de_ingreso":fecha_de_ingreso,"cuota_al_dia":cuota_al_dia}
#Agregue 2 socios
agregrar_socio(4, "Matias Rodriguez", "08202003",False)
agregrar_socio(5, "Vivi Brun", "21102017", True)

# Cantidad de socios del club
print ("El club tiene", len(socios), "socios")
print (socios)

# Registrar que un usuario pago todas las cuotas
def pagar_cuotas(numero_de_socio):
    socios[numero_de_socio]["cuota_al_dia"] = True
numero_socio = int(input("Ingrese el número del socio que ha pagado todas las cuotas: "))
pagar_cuotas(numero_socio)

# Modificar las fechas de ingreso de todos los socios que ingresaron el 21/10/2017
for numero_de_socio in socios:
    if socios[numero_de_socio]["fecha_de_ingreso"] == "21102017":
        socios[numero_de_socio]["fecha_de_ingreso"] = "22102017"

# Funcion para dar de baja a un usuario
def dar_de_baja_socio():
    nombre_y_apellido = input("Ingrese el nombre y apellido del socio que desea dar de baja: ")
    for numero, datos in socios.items():
        if datos["nombre_y_apellido"] == nombre_y_apellido:
            del socios[numero]
            print(f"El socio {nombre_y_apellido} ha sido eliminado del listado.")
            return
    print(f"No se encontró ningún socio con el nombre {nombre_y_apellido}.")

def imprimir_listado_socios(socios):
    print('Listado completo de socios:')
    for numero, datos in socios.items():# es una forma conveniente de iterar sobre un diccionario y 
        #acceder tanto a las claves como a los valores asociados a ellas. Devuelve una lista de tuplas
        nombre_y_apellido = datos['nombre_y_apellido']
        fecha_de_ingreso = datos['fecha_de_ingreso'][0:2] + '/' + datos['fecha_de_ingreso'][2:4] + '/' + datos['fecha_de_ingreso'][4:]
        # Se extraen los valores. por ej datos['fecha_de_ingreso'][0:2] extrae los primeros dos caracteres 
        # de la cadena, que corresponden al año. Y despues se separa con una barra, el fin es que sea mas legible
        cuota_al_dia = 'Sí' if datos['cuota_al_dia'] else 'No'
        print(f'Socio número {numero}, {nombre_y_apellido}, ingresó el {fecha_de_ingreso}, cuota al día: {cuota_al_dia}')
imprimir_listado_socios(socios)


