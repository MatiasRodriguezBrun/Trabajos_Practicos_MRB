#!/usr/bin/ env python3
# esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20.
class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5
    
    def encontrarPilaAtomica(self):
        self.potencia += 25
        if self.potencia > 100:
            self.potencia = 100
    
    def encontrarEscudo(self):
        self.coraza +=10
        if self.coraza > 20:
            self.coraza = 20

    def recibirAtaque(self, puntos):
        if puntos >= self.coraza:
            self.potencia += self.coraza - puntos
            self.coraza = 0
        else:
            self.coraza -= puntos

    def fortalezaDefensiva(self):
        return (self.coraza + self.potencia)
    
    def necesitaFortalecerse(self):
        return bool (self.coraza == 0 and self.potencia < 20)
    
    def fortalezaOfensiva(self):
        if self.potencia < 20:
            return 0
        else:
            return (self.potencia-20)/2

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
print ("Luego de encontrar la pila, cual es su potencia?", enterprise.potencia)
print ("Y su coraza?", enterprise.coraza)
print(enterprise.fortalezaDefensiva())
print(enterprise.necesitaFortalecerse())
print(enterprise.fortalezaOfensiva())

"""
enterprise.encontrarPilaAtomica()
print ("Luego de encontrar la pila, cual es su potencia?", enterprise.potencia)
print ("Y su coraza?", enterprise.coraza)

enterprise.recibirAtaque(22)
print ("Recibio un ataque, cual es su potencia?", enterprise.potencia)
print ("Y su coraza?", enterprise.coraza)

enterprise.encontrarEscudo()
print (enterprise.potencia)
print (enterprise.coraza)
"""
