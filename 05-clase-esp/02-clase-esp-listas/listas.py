# Las colecciones en python (arreglos)

"""
listas []
    es una coleccion ordenada, es modificable, permite miembros duplicados
tuplas ()
    es una coleccion ordenada, no es modificable, permite miembros duplicados
set {}
    es una coleccion no es ordenada, no es indexada, no permite miembros duplicados
diccionario {key=value}
    es una coleccion no es ordenada, es modificable, es indexado, no permite miembros duplicados
"""
# listaEstudiantes = []
# listaEstudientes = ["balbino", "diego", "keavy", "fatima"]
# print(listaEstudientes)

# como accedemos a un miembro individual
# listaEstudientes = ["balbino", "diego", "keavy", "fatima"]
# print(listaEstudientes[2])

# indexado negativo
# listaEstudientes = ["balbino", "diego", "keavy", "fatima"]
# print(listaEstudientes[-1])

# hacer un rango de indices (slicing)
# listaEstudientes = [
#     "balbino",
#     "diego",
#     "keavy",
#     "fatima",
#     "gabriela",
#     "valeria",
#     "rodrigo",
# ]
# print(listaEstudientes[2:5])
# print(listaEstudientes[:])
# print(listaEstudientes[:5])
# print(listaEstudientes[2:])
# print(listaEstudientes[::2])


# cambiar un elemento de la lista
# listaEstudientes = [
#     "balbino",
#     "diego",
#     "keavy",
#     "fatima",
#     "gabriela",
#     "valeria",
#     "rodrigo",
# ]
# listaEstudientes[0] = "sven"
# print(listaEstudientes)

# como navegar a traves de una lista
# listaEstudientes = [
#     "balbino",
#     "diego",
#     "keavy",
#     "fatima",
#     "gabriela",
#     "valeria",
#     "rodrigo",
# ]
# for person in listaEstudientes:
#     person += "x"
#     print(person)

# revisar si un elemento existe en la lista
# listaEstudientes = [
#     "balbino",
#     "diego",
#     "keavy",
#     "fatima",
#     "gabriela",
#     "valeria",
#     "rodrigo",
# ]

# if "rodrigo" in listaEstudientes:
#     print("rodrigo es la mayor nota de la materia")


# como encontramos el tamanio de una lista
# listaEstudientes = [
#     "balbino",
#     "diego",
#     "keavy",
#     "fatima",
#     "gabriela",
#     "valeria",
#     "rodrigo",
# ]
# print(len(listaEstudientes))


# como encontramos el tamanio de una lista
# listaEstudientes = ["balbino", "diego", "keavy"]
# listaEstudientes.append("rodrigo")
# listaEstudientes.append("valeria")
# listaEstudientes.append("gabriela")
# print(listaEstudientes)
# listaEstudientes.insert(1, "fatima")
# print(listaEstudientes)
# listaEstudientes.remove("diego")
# print(listaEstudientes)

"""
    pop()
    del listaEstudiantes[5]
    clear()
    copy()

"""
# x = [1, 2, 3]
# y = [4, 5]
# result = x + y
# print(result)