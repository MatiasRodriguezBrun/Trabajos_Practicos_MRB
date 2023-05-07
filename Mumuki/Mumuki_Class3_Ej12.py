#!/usr/bin/ env python3
class Chef:
    def __init__(self, plato_del_dia):
        self.plato_del_dia = plato_del_dia

    def picantear(self):
        if not self.plato_del_dia.demasiado_picante():
            self.plato_del_dia.picantear()
        else:
            raise Exception("El plato ya está demasiado picante")

class AyudanteDeCocina:
    def suavizar(self, plato):
      self.plato = plato
      self.plato.suavizar()

class Pasta:
    def __init__(self):
        self.ajies = 0

    def demasiado_picante(self):
        return self.ajies > 10
    
    def picantear(self):
      self.ajies += 5
      
    def suavizar(self):
      self.ajies -= 1 

class Pizza:
    def __init__(self):
        self.condimento = "adobo"

    def demasiado_picante(self):
        return self.condimento == "cayena"
      
    def picantear(self):
      self.condimento = "cayena"
      
    def suavizar(self):
      self.condimento = "oregano"
  

      

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