#!/usr/bin/ env python3
class MedioDeTransporte:
  def __init__(self, combustible):
    self.combustible = combustible
    
  def cargar_combustible(self, combustible_nuevo):
    self.combustible += combustible_nuevo
  
  def entran_personas(self, personas):
    
    
class Auto(MedioDeTransporte):
    def maximo_personas(self):
      return self.entran_personas(5)
    
    def recorrer(self, kilometro):
      self.combustible -= kilometro/2
      
class Moto(MedioDeTransporte):     
    def maximo_personas(self):
      return self.entran_personas(2)

    def recorrer(self, kilometro):
      self.combustible -= kilometro      

car = Auto(10)
print("Combustible de car antes de recorrer ", car.combustible)
car.recorrer(2)
print("Combustible de car despues de recorrer ", int(car.combustible))
print (car.entran_personas(4))