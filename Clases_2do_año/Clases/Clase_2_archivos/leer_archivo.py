#armar un scrip que lea el archivo "archivo.txt" y crear otro archivo que va 
# a contener los primeros 5 caracteres del archivo anterior

with open ("Clases/archivo.txt", "r") as mi_arch:
    with open ("Clases/archivo.txt", "a") as nuevo:
        nuevo.write(mi_arch.readline(5))

texto_leido = open ("Clases/archivo.txt", "r").read()
  
print (texto_leido)

print (texto_leido[0:6])

with open ("nuevo_archivo.txt", "a") as mi_arch:
    mi_arch.write(texto_leido[0:6])


