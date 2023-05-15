#!/usr/bin/ env python3
import os, sys, re, glob

#Ejercicio de Practica
# Escribir un script en el cual debemos movernos a la carpeta Informes y obtener los archivos *.txt que hayan allí.
# Por cada archivo hay que obtener, por un lado, cuántas veces aparece la palabra "estado" y por otro lado la 
# cantidad de líneas. Por último, hay que crear una carpeta que se llame Apellidos, donde hay que crear un archivo 
# llamado Lista.txt que contenga en cada línea la primer línea de cada archivo .txt obtenidos anteriormente.
def carpeta():
    os.chdir("../Informes")
    txt = glob.glob("*.txt")
    cant_estado = []
    cant_lineas = []
    for archivo in txt:
        with open (archivo, "r") as file:
            txt_leido = file.read()
            cant_estado.append(txt_leido.count("Estado"))
            cant_lineas.append(txt_leido.count("\n"))
    print("cantidad de estado:", cant_estado)  
    print ("En el primer archivo aparece",cant_estado[0], "veces la palabra Estado. Y tiene", cant_lineas[0], "lineas")
    print("cantiadad total de estado", sum(cant_estado))     
    print("cantidad de lineas:",cant_lineas) 
    print("cantiadad total de lineas", sum(cant_lineas))  

    if not os.path.exists("Apellidos"):
        os.mkdir("Apellidos")
    else:
        print ("No se puede crear porque la carpeta Apellidos porque ya existe")

    with open ("Apellidos/Lista.txt", "w") as salida:
        for archivo in txt:
            with open(archivo, "r") as file:
                primer_linea = file.readline()
                salida.write(primer_linea)

#Ejercicio 1
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una 
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P")
with open("archivo_ej1.txt  ", "r") as miarch:
    contador = 0
    for linea in miarch:
        if not linea.startswith("P"):
                contador += 1
    print(contador, "lineas no comienzan con la letra P")

#Ejercicio 2
# Escribí un programa que lea un archivo e imprima las primeras n líneas.
# range (a(inicio),b(fin),c(paso)) --> por defecto arranca en 0 y el paso es uno
# (para aclarar el paso es necesario poner el inicio) En caso de querer que vaya para atras (0,4,-1)
def read_n_lines(n, archivo):
    with open(archivo, "r") as miarch:
        for linea in range(n):
            print (miarch.readline()) #print (linea.replace("\n",""))

read_n_lines(3, "archivo_ej1.txt")

#Ejercicio 3
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista 
# y luego imprima las n últimas.
def ej3(archivo, n):
    # Abrimos el archivo en modo lectura usando la función 'open' de Python.
    # El archivo se cierra automáticamente al salir del bloque 'with'.
    with open(archivo, "r") as miarch:
        # Leemos todas las líneas del archivo y las almacenamos en la variable 'lista_de_lineas'.
        lista_de_lineas = miarch.readlines()
        # Usando la técnica de "rebanado de listas", obtenemos las últimas 'n' líneas de la lista.
        # Luego, usamos un bucle 'for' para imprimir cada una de estas líneas.
        for linea in lista_de_lineas[-n:]:
            # Imprimimos la línea sin agregar un salto de línea adicional al final.
            # El parámetro 'end' se establece en una cadena vacía para lograr esto.
            print(linea, end="")

# Llamamos a la función 'ej3' y le pasamos el nombre del archivo y el número de líneas a imprimir.
(ej3("archivo_ej1.txt", 2))

def imprimir_las_n_ultimas(n, archivo):
    with open (archivo, "r") as miarch:
        archivo_leido = miarch.readlines()
        lista = []
        for linea in archivo_leido[-n:]:
            lista.append(linea)
        print (lista)   
imprimir_las_n_ultimas(2, "archivo_ej1.txt")

#Ejercicio 4
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
def cantidad_de_palabras(archivo):
    with open(archivo, "r") as file:
        contador = 0
        file = file.read()
        for linea in file: 
            contador += len(linea.split()) #Separa la línea en palabras usando la función split(), 
            # cuenta cuántas palabras hay y las agrega al contador
    return contador
print(cantidad_de_palabras("archivo_ej1.txt"))

#Ejercicio 5
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y 
# lo guarde en otro archivo.
def reemplazar_y_guardar(archivo_entrada, archivo_salida, letra_a_reemplazar):
    with open(archivo_entrada, "r") as file_in:
        # Abre el archivo de salida en modo escritura
        with open(archivo_salida, "w") as file_out:
            # Itera por cada línea del archivo de entrada
            for linea in file_in:
                # Reemplaza la letra especificada por la misma letra más un salto de línea
                nueva_linea = linea.replace(letra_a_reemplazar, letra_a_reemplazar + '\n')
                # Escribe la nueva línea en el archivo de salida
                file_out.write(nueva_linea)

# Llama a la función reemplazar_y_guardar() con los nombres de archivo y letra a reemplazar como argumentos
reemplazar_y_guardar("archivo_ej1.txt", "archivo_salida.txt", "a")

#Ejercicio 6
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
def eliminar_saltos_de_linea(archivo_de_entrada, archivo_salto_de_linea):
    with open(archivo_de_entrada, "r") as file_entrada:
        with open(archivo_salto_de_linea, "a") as file_salida:
            for linea in file_entrada:
            # Elimina los saltos de línea al final de cada línea
                linea_sin_saltos = linea.strip()
            # Escribe la línea sin saltos de línea en el archivo de salida, seguida de un salto de línea
                file_salida.write(linea_sin_saltos + '\n')
eliminar_saltos_de_linea("archivo_ej1.txt", "archivo_salto_de_linea.txt")

#Ejercicio 7
# Escribí un programa que lea un archivo e identifique la palabra más larga, la cual
# debe imprimir y decir cuantos caracteres tiene.
# split() --> por defecto separa el string por espacios en blanco. Ej: "Clase 5 de abril" --> ["CLase","5","de","Abril"]
def ejercicio(archivo):
    with open (archivo, "r") as file:
        txt_leido = file.read().split()
    lista = []
    for palabra in txt_leido:
        lista.append(len(palabra))
    caracteres_de_palabra_mas_larga = max(lista)
    posicion_de_palabra_mas_larga = (lista.index(max(lista)))
    print ("La palabra mas larga es", txt_leido[posicion_de_palabra_mas_larga]," y tiene", caracteres_de_palabra_mas_larga, "caracteres")

ejercicio("archivo_ej1.txt")

#Ejercicio 8
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
def combinar_archivos(archivo1, archivo2, archivo_salida):
    with open(archivo1, "r") as file1, open(archivo2, "r") as file2, open(archivo_salida, "a") as file_salida:
        contenido1 = file1.read()
        contenido2 = file2.read()
        file_salida.write(contenido1)
        file_salida.write(contenido2)

#Ejercicio 9
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra
# en cuestión con respecto a la cantidad total de palabras.
def obtener_frecuencia(archivo):
    with open(archivo, "r") as file:
        # Leer el archivo y guardar su contenido en una lista
        contenido = file.read().split()
        
        # Limpiar la lista de caracteres no deseados
        caracteres_no_deseados = ["\n", ".", ",", ";", ":", "!", "?"]
        contenido = [palabra.strip("".join(caracteres_no_deseados)).lower() for palabra in contenido]
        
        # Iterar sobre la lista y guardar la cantidad de veces que aparece cada palabra en un diccionario
        frecuencia = {}
        for palabra in contenido:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
        
        # Calcular la frecuencia de cada palabra y guardarla en otro diccionario
        total_palabras = len(contenido)
        frecuencia_relativa = {palabra: (frecuencia[palabra]/total_palabras)*100 for palabra in frecuencia}
        
        # Imprimir los resultados
        print("Frecuencia absoluta de cada palabra:")
        for palabra, cantidad in frecuencia.items():
            print(f"{palabra}: {cantidad}")
            
        print("\nFrecuencia relativa de cada palabra (%):")
        for palabra, frecuencia in frecuencia_relativa.items():
            print(f"{palabra}: {frecuencia}")
        
#Ejercicio 10
# Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo
# dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
# (NO ES DE LA CONSIGNA ORIGINAL) Encontrar los mails y escribirlos en una archivo nuevo

def carpeta(archivo_salida, archivo_salida_solo_mails):
    os.chdir("Carpeta1")
    if not os.path.exists("Resultado"):
        os.mkdir("Resultado")
    else:
        print ("No se puede crear porque la carpeta Resultado ya existe")

    txt = glob.glob("*.txt")
    print (txt)
    for archivo in txt:
        with open (archivo, "r") as entrada:
            texto_leido = entrada.read()
    
        os.chdir("Resultado")
        with open (archivo_salida, "a") as salida: # se usa append xq lo estoy recorriendo sino solo me escribiria 
                                                   # el contenido del ultimo archivo                                          
            salida.write(texto_leido + "\n") # + "\n" agrega el salto de linea
        os.chdir("../") # para que vuelva a la carpeta inicial, en este caso Informes y busque el siguiente archivo
                        # alli y no en la carpeta nueva("Resultado")
    
    mails = re.findall(r"[a-z]+[._-][0-9]*[a-z]*[@][a-z]+[.][a-z]+[.]?[a-z]{2,3}", archivo_salida)
    os.chdir("Resultado")
    with open (archivo_salida_solo_mails, "a") as mails:
        for mail in mails:
            mails.write(mail + "\n")

#ej 1 variante
def ej1(archivo):
    with open(archivo, "r") as miarch:
        texto = miarch.read()
        empieza_con_p = re.findall(r"[P]", texto)
        print ("Sabemos que", len(empieza_con_p), "lineas empiezan con P")

    with open (archivo, "r") as miarch2:
        leido_en_lista = miarch2.readlines()
        print ("Sabemos que el archivo total tiene", len(leido_en_lista), "lineas")

        lineas_no_empiezan_con_p = len(leido_en_lista) - len(empieza_con_p)
        print (f"Por lo tanto {lineas_no_empiezan_con_p} lineas no empiezan con la letra P")

ej1("tipo_de_sangre.txt")  
 
