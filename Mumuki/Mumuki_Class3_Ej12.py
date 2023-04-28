#!/usr/bin/ env python3

class Chef:
  def __init__(self, plato_del_dia):
    self.plato_del_dia = plato_del_dia
    
  def picantear(self, plato):
    if plato is not demasiado_picante():
      return True
    else:
      raise Excep ("El plato ya está demasiado picante")
  
class AyudanteDeCocina:
  def suavizar(self, plato):
    return True

class Pasta:
  def __init__(self):
    self.ajies = 0

    
  def demasiado_picante(self):
      return self.ajies > 10
    
class Pizza:
  def __init__(self):
    self.condimento = "adobo"

  def demasiado_picante(self):
    return self.condimento == "cayena"

"""
fideos = Pasta()
muzzarella = Pizza()
jor = Chef(fideos)
luchi = AyudanteDeCocina()
jor.picantear()
luchi.suavizar(fideos)
jor.plato_del_dia = muzzarella
luchi.suavizar(muzzarella)
jor.picantear()
"""