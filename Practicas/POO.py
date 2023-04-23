#Ejercicio 1
#Dada la siguiente clase, identificá la interfaz y el estado de la misma:

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
# clase = self._alimento y self._caricias 
# interfaz = energia, comer, acariciar, estaDebil   
