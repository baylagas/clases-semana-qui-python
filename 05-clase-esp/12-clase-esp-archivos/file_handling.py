import os
import json

"""
tema: manejo de archivos

es una parte muy importante de cualquier tipo de aplicacion
python tiene varias funciones para crear, leer, actualizar y eliminar archivos.

la funcion mas importante para este proposito en python es el metodo open()
este metodo recibe 2 parametros: uno es el filename y otro el mode

hay 4 diferentes tipos de modo

"r" - read - por defecto esta en este modo, da error si el archivo no existe
"a" - append - abre un archivo para agregarle informacion, crea el archivo si no existe
"w" - write - abre un archivo para escribir en el, si el archivo no existe lo crea
"x" - create - crea el archivo pedido, regresa un error si el archivo ya existe

una modalidad para texto o para leer binario
"t" - text - este es el modo por defecto
"b" - binario como cuando queremos leer archivos de imagenes o sonido.

"""

# fileMessage = open(
#     "F:\\Projects\\Python\\_repos\\clases-semana-qui-python\\05-clase-esp\\12-clase-esp-archivos\\demo.txt"
# )
# print(fileMessage)
# print(type(fileMessage))

# # fileMessage = open("demo.txt", "rt")

# # print(fileMessage.read())

# # print(fileMessage.read(8))

# # print(fileMessage.readline())
# # print(fileMessage.readline())
# # print(fileMessage.readline())

# for line in fileMessage:
#     print(line + "x")
# fileMessage.close()


"""
creacion y escritura

"""
# newFile = open(
#     "F:\\Projects\\Python\\_repos\\clases-semana-qui-python\\05-clase-esp\\12-clase-esp-archivos\\demofile2.txt",
#     "a",
# )
# newFile.write("\nviene un huracan")
# newFile.close()


# newFile = open(
#     "F:\\Projects\\Python\\_repos\\clases-semana-qui-python\\05-clase-esp\\12-clase-esp-archivos\\demofile2.txt",
#     "r",
# )
# print(newFile.read())

"""
eliminar archivos
para eliminar archivos podemos ocupar de la libreria os el metodo remove

"""
# newFile = open(
#     "F:\\Projects\\Python\\_repos\\clases-semana-qui-python\\05-clase-esp\\12-clase-esp-archivos\\demofile2.txt",
#     "x",
# )
# newFile.close()

# os.remove(
#     "F:\\Projects\\Python\\_repos\\clases-semana-qui-python\\05-clase-esp\\12-clase-esp-archivos\\demofile2.txt"
# )

"""
para saber si existe un archivo ocupando python

"""
# filePath = "F:\\Projects\\Python\\_repos\\clases-semana-qui-python\\05-clase-esp\\12-clase-esp-archivos\\"
# file01 = "demofile2.txt"

# if os.path.exists(filePath + file01):
#     os.remove(filePath + file01)
# else:
#     print("el archivo no existe")

# """
# eliminar un folder

# """
# os.rmdir(filePath + "example")


"""
manejo de archivos con json

"""
filePath = "F:\\Projects\\Python\\_repos\\clases-semana-qui-python\\05-clase-esp\\12-clase-esp-archivos\\"

with open(filePath + "config.json", "rt") as configFile:
    configString = configFile.read()
    configDict = json.loads(configString)
    print(configDict["user"], configDict["env"])
    configFile.close()
