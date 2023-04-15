#!/usr/bin/ env python3
from aves import pepita, anastasia, roberta
# pepiita sabe volar porqie lo hace sin quejarse
#print(pepita.volar_en_circulos())
# pepita no sabe hablar, ademas aprendimos que pepita es una golondrina
#print (pepita.hablar())
# A pepita le gusta comer alpiste
#print(pepita.comer_alpiste(200))

"""
Sabemos que pepita es un objeto individual/unico, en particular es un objeto de la clase Golondrinas
Que entienden mensajes (los que entieneden las golondrinas) y que tiene las carac de una Golondrina (atributos)
"""
"""
print ("Pepita al comienzo", pepita.energia)
pepita.volar_en_circulos()
print ("despues de volar", pepita.energia)
pepita.comer_alpiste(20)
print ("despues de comer", pepita.energia)
print("Hasta aca Pepita")
"""
"""
Pepita tiene una energia basal
Ahora sabemosque pepita cuando le damos ordenes, esta haciendo algo
y algo es su estado cambia (la energia)
- Entonces ahora sabemos que el estado de pepita esta dado por su energia
- Pepita tiene como atributos o carac saber volar y comer alpiste
- El estado de los objetos de alguna forma puede cambiar o modificarse
"""
"""
print("En el caso de anastasia tiene de energia: ", anastasia.energia)
print(anastasia.volar_en_circulos())
print(anastasia.energia)
print(anastasia.comer_alpiste(200))
print(anastasia.energia)
print(anastasia)
"""
"""
Los objetos pueden tener distintos estados basales, uno propio para cada uno
Aun con distintos estados, los objetos pueden entender los mismos mensajes(se llaman metodos)
"""

print("En el caso de anastasia tiene de energia: ", roberta.energia)
print(roberta.volar_en_circulos())
print(roberta.energia)
# print(roberta.comer_alpiste(200))
roberta.escupir_fuego()
print ("Energia despues de escupir fuego: ",roberta.energia)
roberta.comer_peces(50)
print ("Energia despues de comer peces: ",roberta.energia)
print(roberta)

"""
Hay objetos que entienden los mismos mensajes auqnue no sean de la misma clase
"""
print("Energia de pepita al comienzo: ", pepita.energia)
print (pepita.esta_feliz())
print("Energia del dragon al comienzo: ", roberta.energia)
print (roberta.esta_feliz())
