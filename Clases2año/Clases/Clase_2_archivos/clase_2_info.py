import os, sys


def main():
    pass


def saludoPersonal (mensaje):
  print (f"Hola, ",mensaje)
 
saludoPersonal ("mati")

def saludador():
    nombre = input("decime tu nombre: ")
    print (f"Hola, ",nombre)

saludador ()

#sys.argv toma los argumentos que le pasabamos al scrip por consola,
# [1] significa que siempre voy a tomar el primero 
# es decir solo lee la primer palabra que se escribe en la terminal
usuario = sys.argv[1]

def saludador(nombre):
    return "Hola " + nombre

if __name__ == "__main__" :
    main()
    print(saludador(usuario))


