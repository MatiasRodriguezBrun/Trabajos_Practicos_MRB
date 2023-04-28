#!/usr/bin/ env python3
import re 
# a) Obtener la lista de subsecuencia delimitadas por X e Y que incluyan las subsecuencia "ab". 
# Por ej para XbaaaYjXababYqXbabbbbaaYqXffeeY, hay que devolver ["abab, "babbbaa"]
def obtener_subsecuencia(string):
    return re.findall(r"[^X][ab]+[^Y]", string) # es lo mismo q poner [ab]+
print(obtener_subsecuencia("XbaaaYjXababYqXbabbbbaaYqXffeeY"))

"""
# b) 
def funcionDeExpresiones_Regulares():
    return re.findall("ag(\d.*?)cta")

print(funcionDeExpresiones_Regulares())
"""