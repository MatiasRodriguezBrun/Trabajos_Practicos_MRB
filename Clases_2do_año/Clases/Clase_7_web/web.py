#!/usr/bin/python

import requests, re
# requests es un pedido 

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs") 
# le consulta al servidor no a la base de datos
# get --> lo hace el cliente --> asocia
datos = respuesta.json() #--> es uns estructura de diccionario 
print (datos)
# en cuantas org esta involucrado el usuario
print (len(datos))
# lista de nombres de las org en la que esta involucrado 
print (datos.keys())


print (respuesta.headers) # los headers me da info acerca del request
print(respuesta.status_code) # te da un numero 
"""
def buscar_org():
    for i in datos:
        organizaciones = re.findall("organizaciones", datos)
        return len(organizaciones)
print(buscar_org)
"""

#get es el verbo HTTP asociado a las consultas

# verbos HTTP disparan acciones particulares --> SIEMPRE HABLANDO de aplicaciones RESTS
# Tiene al menos 4 verbos

