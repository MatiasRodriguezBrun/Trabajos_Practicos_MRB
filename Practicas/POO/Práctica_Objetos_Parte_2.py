#!/usr/bin/ env python3

#Ejercicio 1
# Dada la siguiente clase:
# cuales son sus estados. 
# cuales son sus interfaces. 
# ¿Comparten interfaz?
# ¿Son polimórficas?
"""
class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
        print(self.alimento)
    
    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	    self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
        print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4

# El estado es el conjunto de los atributos, por lo tanto el estado del perro y del gato
# es self.alimento y self.caricias 

# La interfaz es el conjunto de mensajes.
# Interfaz gato: energia, comer, caricias, acariciar, estaDebil 
# Interfaz perro: energia, comer, acariciar, estaDebil, pasear, alimentar 

# Comparten parte de su interfaz ya que tienen el mensaje acariciar que se comporta de igual manera en ambas clases.
# Por ello se podria decir que son poliformicas parciales pero la realidad es que haria falta de un tercera clase que envie 
# un mismo mensaje a distintos objetos. La clase que envía el mensaje debe ser una, y al menos 2 que lo reciban.

#Ejercicio 2
# Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio.
# Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.

   def esta_en_equilibrio(self):
    return bool (150 < self.energia < 300)
"""   
#Ejercicio 3 
# Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión
#  (del ejercicio 7 de la práctica anterior), o una golondrina. Un ornitólogo somete, cada vez que lo decide, a cada 
# una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms,
# y finalmente hacerla comer otros 10 gramos. Se propone:

class Ornitologo:
    def __init__(self):
        self.conjunto_de_aves = []
    
    def estudiarAve(self, ave):
        self.conjunto_de_aves.append(ave)

    def avesEnEstudio(self):
        return self.conjunto_de_aves
    
    def realizarRutinaSobreAves(self): 
        self.conjunto_de_aves.comer(80)
        self.conjunto_de_aves.volar(70)
        self.conjunto_de_aves.comer(10)

    def avesEnEquilibrio(self, ave):
        return ave.esta_en_equilibrio() == True

loco = Ornitologo()
gorrioncito = Gorriones()

"""
comprobar el código que se escribió con esta secuencia:

definir un ornitólogo, dos golondrinas y dos gorriones,
inicializar las aves con valores conocidos,
decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
decirle al ornitólogo que realice su rutina sobre aves,
verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.
"""
"""
# Ejercicio 4 

class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, combustible):
        self.combustible += combustible

class Moto(MedioDeTransporte):
    def consumo(self, kilometros):
        self.combustible -= kilometros

    def entran_personas(self, personas):
        return personas <= 2
        
class Auto(MedioDeTransporte):
    def consumo(self, kilometros):
        self.combustible -= kilometros/2
    
    def entran_personas(self, personas):
        return personas <= 5
    
car = Auto(100)
print(car.entran_personas(6))
print(car.entran_personas(2))
"""



