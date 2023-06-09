import requests, re

pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# a) ¿Cuál es el dominio al que estamos consultando?
# El dominio es "pokeapi.co"

# b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente
# al campo "forms".
pikachu.json()
print("El status code de la rta es", pikachu.status_code) 
print ("El content type de la rta es", pikachu.headers["Content-Type"])

print(pikachu.json().keys())
print(pikachu.json()["forms"])


# c) Averigüá cuántos Pokemones almacena la API.
pokemones = requests.get("https://pokeapi.co/api/v2/pokemon/")
contenido_respuesta = pokemones.json() 
print ("La API tiene", (contenido_respuesta["count"]), "pokemones")


# d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? 
# https://pokeapi.co/api/v2/ability --> haciendo referencia a esos recursos 
# ¿y cómo será la url para obtener la información sobre la habilidad 2?
# https://pokeapi.co/api/v2/ability/2

# f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre
#  "ficha_tecnica_pokemon.txt".
# alternativa --> str(pikachu.json()) --> convert to str
sylveon = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")

with open ("ficha_tecnica_pokemon.txt", "wb") as ficha: # modo wb --> escribir bytes
    ficha.write(pikachu.content)
    ficha.write(b"\n")
    ficha.write(sylveon.content)

# g) Describí la arquitectura cliente-servidor y los roles de cada parte

"https://jsonplaceholder.typicode.com/todos"
# a) ¿Cuál es el dominio al que estamos consultando?
# El dom es jsonplaceholder.typicode.com

# b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type?
respuesta = requests.get("https://jsonplaceholder.typicode.com/todos")
# print (respuesta.json())
print("El status code de la rta es", respuesta.status_code) 
print ("El content type de la rta es", respuesta.headers["Content-Type"])

# c) Agregar un contenido cuyo userId es 11 y su id es 2 con un nuevo título e indicando que está completo 
# (completed).
data = ""


# d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?











