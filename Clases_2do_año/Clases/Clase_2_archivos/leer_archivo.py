#armar un scrip que lea el archivo "archivo.txt" y crear otro archivo que va 
# a contener los primeros 5 caracteres del archivo anterior

with open ("archivo.txt", "r") as mi_arch:
    with open ("archivo.txt", "a") as nuevo:
        nuevo.write(mi_arch.readline(5))

texto_leido = open ("archivo.txt", "r").read()
print (texto_leido)
print (texto_leido[0:6])

with open ("nuevo_archivo.txt", "w") as mi_arch:
    mi_arch.write(texto_leido[0:6])


