# diccionarios

# es una coleccion que no tiene orden, es modificable y tambien es indexado.
# no es un indexado numerico
# la estructura de un diccionario se utiliza tambien los {} curly brackets.
# los diccionarios trabajan un una dupla de llave y valor (key/value pair)

# personDic = {"name": "balbino", "age": 23, "salary": 300.0}
# print(personDic)
# print(type(personDic))

# como acceder a un valor de un diccionario
# personDic = {"name": "balbino", "age": 23, "salary": 300.0}
# print(personDic["salary"])
# # como un metodo alternativo se puede usar el metodo get()
# print(personDic.get("name"))

# como cambiar los valores en un diccionario
# personDic = {"name": "balbino", "age": 23, "salary": 300.0}
# personDic["age"] = 25
# print(personDic)

# como navegar el diccionario
# personDic = {"name": "balbino", "age": 23, "salary": 300.0}
# for element in personDic:
#     # print(element)
#     print(personDic[element])

# print(personDic.keys())
# print(type(personDic.keys()))
# for key in personDic.keys():
#     print(personDic[key])

# personDic = {"name": "balbino", "age": 23, "salary": 300.0}
# for value in personDic.values():
#     print(value)

# personDic = {"name": "balbino", "age": 23, "salary": 300.0}
# for key, value in personDic.items():
#     print(key, value)

# personDic = {"name": "balbino", "age": 25, "salary": 300.0}
# if "age" in personDic:
#     if personDic["age"] == 25:
#         print("25 se encontro")

# personDic = {
#     "name": "balbino",
#     "age": 25,
#     "salary": 300.0,
#     "job": "programmer",
#     "color": "black",
# }
# print(len(personDic))

# personDic = {"name": "balbino", "age": 25, "salary": 300.0}
# personDic["job"] = "teacher"
# personDic["color"] = "red"
# print(personDic)

# como removemos elementos de un diccionario
# personDic = {"name": "balbino", "age": 25, "salary": 400.0}
# # pop()
# eliminado = personDic.pop("salary")
# print("eliminado: " + str(eliminado))
# print(personDic)
# personDic["job"] = "teacher"
# personDic["color"] = "red"
# # popitem()
# key, value = personDic.popitem()
# print("eliminado")
# print(key)
# print(value)

# la palabra reservada del elimina una variable completamente de la memoria

# limpiar todo el diccionario el metodo clear()
# personDic = {"name": "balbino", "age": 25, "salary": 400.0}
# personDic.clear()
# print(personDic)

# personDic = {"name": "balbino", "age": 25, "salary": 250.0}
# mycopy = personDic.copy()
# print(mycopy)
# mycopy2 = dict(personDic)
# print(mycopy2)

# business = {
#     "programmer1": {"name": "balbino", "salary": 200.5},
#     "programmer2": {"name": "diego", "salary": 300.5},
# }

# print(business.keys())

# for worker in business:
#     print(worker)
#     print("    ", business[worker])

# newDict = dict(name="rodrigo", age=23, salary=450.0, married=True)
# print(newDict)
