#!/usr/bin/ env python3

class Titan:
    def __init__(self, salud):
        self.salud = salud

    def recibir_ataque(self, daño):
        self.salud -= daño*1.5
    
    def esta_vivo(self):
        return self.salud > 0
    
    def salud_actual(self):
        return self.salud
    
    def cuantas_casas(self):
        return self.salud*8/100
    
    def destruir_casas(self):
        print (self.cuantas_casas()) #duda
    
    def grito(self):
        return "¡Aaaarrrg!"

titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())