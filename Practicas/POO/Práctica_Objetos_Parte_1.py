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
# interfaz: energia, comer, acariciar, estaDebil 
# estado: self._alimento, self._caricias 
   
#Ejercicio 2
# Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no
# pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.
"""
  def volar(self, kms):
    if self.energia <= 0:
        return "No puede volar"
    else:
        self.energia -= 10 + kms
"""  

#Ejercicio 3
# Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento 
# al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver
# cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en 
# algunos casos aplicar este descuento.
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, descuento):
        return  (self.precio - (self.precio*(descuento/100)))

dell = Notebook("dell", "core I5", 18000)

print(dell.descuento(10))


#Ejercicio 4
# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible 
# indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes 
# mensajes:
class Contador:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
        self.ultimo_comando = None
    
    def inc(self):
        self.valor_inicial += 1
        self.ultimo_comando = "incremento"

    def dis(self):
        self.valor_inicial -= 1
        self.ultimo_comando = "disminucion"
    
    def reset(self):
        self.valor_inicial = 0
        self.ultimo_comando = "reset"

    def valorActual(self):
        return self.valor_inicial

    def valorNuevo(self, nuevoValor):
        self.valor_inicial = nuevoValor
        self.ultimo_comando = "actualizacion"

    def ultimoComando(self): #punto 5
        return self.ultimo_comando

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valorActual())
contador.valorNuevo(27)
contador.dis()
contador.dis()
print(contador.valorActual())
print (contador.ultimoComando()) #punto 5

#Ejercicio 5
# Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió,
# en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización"
# (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el
# resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".
"resuelto arriba"

#Ejercicio 6
# Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. 
# Este objeto debe entender los siguientes mensajes:
class Calculadora:
    def __init__(self):
        self.resultado = None
   
    def cargar(self, numero):
        self.resultado = numero
    
    def sumar(self, numero):
        self.resultado += numero

    def restar(self, numero):
        self.resultado -= numero
    
    def multiplicar(self, numero):
        self.resultado *= numero
    
    def valorActual(self):
        return self.resultado

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print(calculadora.valorActual())
# el resultado debe ser 24

#Ejercicio 7
# Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS 
# (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de 
# dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total
#  de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez
#  que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad 
# de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera 
# en equilibrio si su CSS está entre 0.5 y 2.
class Gorriones:
    def __init__(self):
        self.kilometros = [] 
        self.gramos = []

    def volar(self, km):
        self.kilometros.append(km)

    def comer(self, gramos):
        self.gramos.append(gramos)

    def css(self):
        if not self.gramos == []: # if len(self.gramos) > 0: 
            return sum(self.kilometros) / sum(self.gramos) #suma los valores de la lista SOLO si son valores numericos
                                                       # si hay strings rompe
        else:
            return None

    def cssp(self):
        if not self.gramos == []:
            return max(self.kilometro) / max(self.gramos)
        else:
            return None

    def cssv(self):
        if not self.gramos == []:
            return len(self.kilometro) / len(self.gramos)
        else:
            return None
        
    def esta_en_equilibrio(self):
        return  0.5 <= self.css() <= 2 #en lugar de usar un if 
    # en otro lenguaje --> return self.css() >= 0.5 and self.css() =< 2  
        