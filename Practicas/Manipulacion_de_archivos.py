#Ejercicio 1
import os, sys
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una 
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
"""
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
    # Devolvemos la lista completa de líneas para cualquier uso futuro.
    return lista_de_lineas
# Llamamos a la función 'ej3' y le pasamos el nombre del archivo y el número de líneas a imprimir.
print(ej3("archivo_ej1.txt", 3))

#Ejercicio 4
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
def cantidad_de_palabras(archivo):
    with open(archivo, "r") as file:
        contador = 0
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
"""
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
            
"""
#Ejercicio 7
# Escribí un programa que lea un archivo e identifique la palabra más larga, la cual
# debe imprimir y decir cuantos caracteres tiene.
# split() --> por defecto separa el string por espacios en blanco. Ej: "Clase 5 de abril" --> ["CLase","5","de","Abril"]
def palabra_mas_larga(archivo):
    palabra_mas_larga = ""
    longitud_mas_larga = 0
    with open(archivo, "r") as file:
        for linea in file:
            palabras = linea.split()
            for palabra in palabras:
                longitud_palabra = len(palabra)
                if longitud_palabra > longitud_mas_larga:
                    longitud_mas_larga = longitud_palabra
                    palabra_mas_larga = palabra
    print(f"La palabra más larga es '{palabra_mas_larga}' y tiene {longitud_mas_larga} caracteres.")
#Ejercicio 8
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
def combinar_archivos(archivo1, archivo2, archivo_salida):
    with open(archivo1, "r") as file1, open(archivo2, "r") as file2, open(archivo_salida, "w") as file_salida:
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

def concatenar_archivos_txt(carpeta):
    # Crear la carpeta "Resultado" dentro de la carpeta "Carpeta1" (si no existe).
    ruta_carpeta_resultado = os.path.join(carpeta, "Resultado")
    if not os.path.exists(ruta_carpeta_resultado):
        os.makedirs(ruta_carpeta_resultado)

    # Crear un archivo de salida dentro de la carpeta "Resultado".
    ruta_archivo_salida = os.path.join(ruta_carpeta_resultado, "resultado.txt")
    with open(ruta_archivo_salida, "w") as file_salida:
        # Iterar sobre los archivos ".txt" de la carpeta "Carpeta1" y copiar su contenido en el archivo de salida.
        for nombre_archivo in os.listdir(carpeta):
            ruta_archivo = os.path.join(carpeta, nombre_archivo)
            if os.path.isfile(ruta_archivo) and nombre_archivo.endswith(".txt"):
                with open(ruta_arch 
"""