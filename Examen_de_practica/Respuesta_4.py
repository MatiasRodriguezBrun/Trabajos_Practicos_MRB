#!/usr/bin/ env python3

class Pacman:
    def __init__(self, vidas, puntos):
        self.vidas = 3
        self.puntos = puntos

    def puntos_bolitas(self, bolitas):
        self.puntos += bolitas
    
    def puntos_fantasmas(self,fantasma):
        self.puntos += fantasma.puntos_que_otorga()
    #puntos que obtiene comiendo bolitas
    #puntos que obtiene al comerse un fantasma

class Fantasma:
    def __init__(self, puntos_que_otorga):
        self.puntos_que_otorga = puntos_que_otorga
    

rosa = Fantasma(8)
verde = Fantasma(6)
naranja = Fantasma(4)
rojo = Fantasma(2)

print("El fantasma rosa otorga:", rosa.puntos_que_otorga, "puntos")