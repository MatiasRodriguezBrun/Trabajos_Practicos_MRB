#!/usr/bin/ env python3

# super y dos ejemplos de uso

class Saludo:
  def saludar(self):
    return "Buen día"

class SaludoDocente(Saludo):
  def saludar(self):
    return super().saludar() + " estudiantes"

class Colectivo(MedioDeTransporte):
  def __init__(self):
    self.combustible = 100
    self.pasajeros = 0
  
  def entran_personas(self,personas): 
    return True
  
  def recorrer(self, kilometros):
    self.combustible -= kilometros*2
    
  def cargar_combustible(self, combustible_nuevo):
    super().cargar_combustible(combustible_nuevo) 
    self.pasajeros = 0
