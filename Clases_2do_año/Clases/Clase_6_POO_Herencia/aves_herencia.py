class AnimalAlado:
  def esta_feliz(self):
    return self.energia > 500

class Golondrina(AnimalAlado): # significa que hereda de otra clase, entiende los mensajes de esa clase de la cual hereda
    #estado del objeto
  def __init__(self, energia): #constructor del objeto
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
  
  def esta_feliz(self):
    return self.energia>50

  def esta_debil(self):
    return self.energia < 10 


class Dragon(AnimalAlado):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_feliz(self):
    return self.energia>500
  
  def esta_debil(self):
    return self.energia < 50 

class Entrenador:
  def __init__(self, equipo_dragones):
    self.equipo_dragones = equipo_dragones # una lista de objetos 

  def aceptar_dragones(self, dragon):
    self.equipo_dragones.append(dragon)

  def entrenar(self, equipo_dragones):
    for dragon in self.equipo_dragones:
      dragon.volar_en_circulos() 
      dragon.comer_peces(3)
  
  def entrenamiento_intensivo(self, animal):
    while not animal.esta_debil:
      animal.volar_en_circulos()

    

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
maria = Golondrina(42)
chimuelo = Dragon(200, 1000)
hipo = Entrenador([roberta])
messi = Dragon(10, 700)

# Equipo de Hipo al principio 
print(hipo.equipo_dragones)
# Hipo agrega al dragon "messi" en su equipo
hipo.aceptar_dragones(messi)
print(hipo.equipo_dragones)

#Entrenar 
print("La energia de roberta ANTES del entrenamiento es de: ", roberta.energia)
print("La energia de messi ANTES del entrenamiento es de: ", messi.energia)
hipo.entrenar(roberta)
print("La energia de roberta DESPUES del entrenamiento es de: ", roberta.energia)
print("La energia de messi DESPUES del entrenamiento es de: ", messi.energia)

