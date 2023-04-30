#!/usr/bin/ env python3

class Personas: 
    def __init__(self, energia):
        self.energia = energia
        self.feliz = False # self.estado = "No feliz"

    def dormir(self, horas):
        self.energia += horas*12.5
    
    def comer(self):
        self.energia += 10
        
    def hacer_ejercicio(self, bloques): #los bloques son de media hora c/u
        self.energia -= (bloques*25)/30
    
    def energia_actual(self):
        return self.energia

class Estudiante(Personas):
    def estudiar(self, horas_de_estudio):
        self.energia -= 20*horas_de_estudio

    def aprobar(self):
        return self.feliz == False
    

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())