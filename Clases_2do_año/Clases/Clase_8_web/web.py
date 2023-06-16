#!/usr/bin/python

import requests

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print (respuesta)

print (respuesta.headers)

# 1) Describir las partes de la url 

"""La url esta formada por el https que es el PROTOCOLO y la S es de security 
para que sea rest en akgun punyo las url tienen que de alguna manera mapear recursos, y los recursos son las cosas
(el tipo de cosas) que puedo consultar en la base de datos. Por ej, en meli cuando buscabamos distintos productos y cada 
vez que buscabaos algo distinto en la parte de recurso en la url cambiaba"""

# 2) Qué respuesta obtenes al hacer un get a esa url? 
contenido_respuesta = respuesta.json() 
print (contenido_respuesta.keys())
"<Response [200]>, nos da todo el contenido de esa respuesta"

# 3) Cual es el content type de la respuesta?
"application/json"
print ("El content type de la rta es", respuesta.headers["Content-Type"])

# 4) Cual es el status code de la rta? 
print("El status code de la rta es", respuesta.status_code)

# 5) Cuantas habilidades (abilities) tiene este pokemon?
print (len(contenido_respuesta["abilities"]))
