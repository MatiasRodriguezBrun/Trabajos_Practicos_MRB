#!/usr/bin/ env python3
class MedioDeTransporte:
        def __init__(self, combustible):
          self.combustible = combustible
        
        def cargar_combustible(self, combustible_nuevo):
          self.combustible += combustible_nuevo
    
        def entran_personas(self, personas):
          return personas <= self.capacidad
    
class Auto(MedioDeTransporte):
      
    def recorrer(self, kilometro):
      self.combustible -= kilometro/2
    
    def maximo_personas(self):
      self.capacidad = 5
      
class Moto(MedioDeTransporte):      
    def recorrer(self, kilometro):
      self.combustible -= kilometro      
      
    def maximo_personas(self):
      self.capacidad = 2

car = Auto(10)
car.recorrer(2)
print(car)