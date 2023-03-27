'''
¡Desafío final! Creá un script swap.py que tome dos nombres de archivo y renombre 
al primero con el nombre del segundo, y al segundo lo renombre con el nombre del primero. Ejemplo:
'''
#!/bin/python3
import os

file1 = "hola.txt"
file2 = "chau.txt"

os.rename(file1, "temporal")
os.rename(file2, file1)
os.rename("temporal", file2)

"""
tareas : modificar este scrip para que pueda incorporar los nombres de los
archivos desde la terminal
usar (os.path.exists)--> path 
ver como se usa para mejorar el scrip (basicamente corrobora que el archivo exista)

"""









