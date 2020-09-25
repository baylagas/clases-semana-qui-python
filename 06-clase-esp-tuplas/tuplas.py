# Tuplas

# una tupla es una coleccion que es ordenada no es cambiable.
# se usa con los parentesis ( )

# registro = ("apple", "banana", "cherry")
# registro = ()
# print(registro)

# como acceder a los items de una tupla
# registro = ("apple", "banana", "cherry")
# print(registro[1])

# indexado negativo en una tupla
# registro = ("apple", "banana", "cherry")
# print(registro[-3])

# podemos utilizar notacion de slicing en una tupla
# registro = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # print(registro[2:5])
# # print(registro[2:])
# # print(registro[:5])
# print(registro[::2])

# tambien se puede utilizar indices negavitos con slicing de tuplas

# como hacer un cambio en los valores de una tupla
# registro = ("apple", "banana", "cherry")
# listaRegistro = list(registro)
# print(listaRegistro)
# listaRegistro[1] = "kiwi"
# registro = tuple(listaRegistro)
# print(registro)

# como navegar los elementos de una tupla
# registro = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# for fruta in registro:
#     fruta += " in sale today"
#     print(fruta)

# como revisar la existencia de un item en una tupla
# registro = ("apple", "kiwi", "cherry")
# if "kiwi" in registro:
#     print("Yes, 'kiwi' is in the fruits tuple")

# como obtener la longitud de una tupla
# registro = ("apple", "banana", "kiwi", "cherry")
# print(len(registro))

# agregar un item a una tupla genera un error
# registro = ("apple", "banana", "cherry")
# registro[3] = "orange"  # This will raise an error
# print(registro)

# como crear una tupla de un elemento
# registro = ("apple",)
# print(type(registro))
# registro = "apple"
# print(type(registro))

# en una tupla no podemos remover ningun elemento
# registro = ("apple", "banana", "cherry")
# del registro
# print(registro)

# la union de dos tuplas
# registro1 = ("a", "b", "c")
# registro2 = (1, 2, 3)
# resultado = registro1 + registro2
# print(resultado)

# el metodo constructor = tuple()
# registro = tuple(("apple", "banana", "cherry"))
# print(registro)
# print(type(registro))
