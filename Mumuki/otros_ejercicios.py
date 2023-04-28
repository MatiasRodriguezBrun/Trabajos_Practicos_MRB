class Sobreviviente:
  def __init__(self, adrenalina):
    self.adrenalina = adrenalina
    
  def atacar(self, contrincante):
    if not contrincante.es_un_peligro():
      ataque = self.adrenalina / 2
      contrincante.recibir_danio(ataque)
      self.adrenalina += 20

class Sobreviviente:
  def __init__(self, adrenalina):
    self.adrenalina = adrenalina
    
  def atacar(self, contrincante):
    if not contrincante.es_un_peligro():
      ataque = self.adrenalina / 2
      contrincante.recibir_danio(ataque)
      self.adrenalina += 20
    else:
      raise Exception("Es peligroso atacar a este zombi.")
class PlantaCarnivoraZombi:
  def __init__(self, clorofila):
    self.clorofila = clorofila
  
  def es_un_peligro(self):
    return self.clorofila > 40
  
  def hacer_fotosintesis(self, minutos):
    self.clorofila += minutos
    
  def recibir_danio(self, danio):
    self.clorofila -= 10


class EstudianteDeVeterinaria:
  def alimentar(self, animal, gramos):
    animal.comer(gramos)

  def rehabilitar(self, animal):
    animal.recibir_rehabilitacion() 

class Gato:
  def __init__(self,una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad

  def comer(self,gramos):
    self.energia += gramos

  def cumplir_anios(self):
    self.edad += 1
  def recibir_rehabilitacion(self):
    self.comer(400)
    