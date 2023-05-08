
class PacMan:
    def __init__(self):
        self.vidas = 3
        self.puntos = 0
    
    def velocidad(self):
        return (2 * self.puntos)/100

    def comer_bolitas(self,bolitas):
        self.puntos += bolitas
        self.velocidad +=bolitas
    
    def comer_fantasmas(self,fantasma):
        self.puntos += fantasma.morir() 
        self.velocidad += fantasma.morir() 

    def me_toco_un_fantasma(self,fantasma):
        if self.esta_vivo():
            self.vidas -= fantasma.quitar_vida()
        else:
            raise Exception ("Tu Pacman ha Muerto!")

    def esta_vivo(self):
        return self.vidas < 0

    def nuevas_habilidades(self):
        if self.puntos > 200: 
            self.vidas += 1
        else: pass
        

class Fantasmas:
    def __init__(self,puntos):
        self.puntos = puntos

    def morir(self):
        return self.puntos

    def quitar_vida(self):
        return 1

class FantasmasAterradores(Fantasmas):
    def quitar_vida(self):
        return 2


pacquito = PacMan()

fantasma_rosa = Fantasmas(8)
fantasma_verde = Fantasmas(6)
fantasma_naranja = Fantasmas(4)
fantasma_rojo = Fantasmas(2)
fantasma_multicolor = FantasmasAterradores(10)



print(pacquito.esta_vivo)
print(pacquito.vidas)
pacquito.me_toco_un_fantasma(fantasma_multicolor)
pacquito.me_toco_un_fantasma(fantasma_rosa)
print(pacquito.vivo)
print(pacquito.vidas)
pacquito.me_toco_un_fantasma(fantasma_rosa)
print(pacquito.vidas)

print(pacquito.esta_vivo)