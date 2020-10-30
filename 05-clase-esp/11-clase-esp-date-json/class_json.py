import json

"""
Json en python
json es una sintaxis para guardar y intercambiar informacion
json es text escrito en notacion de objetos de javascript
python tiene una libreria propia para poder leer un json
"""

"""
como trasformar un json a python
si tenemos una cadena en formato json la podemos convertir en en
una coleccion de python con el metodo json.loads() el resultado
sera un diccionario
"""

# # algun json
# jsonString = '{"name":"john", "age":30, "city":"new york"}'

# # convertir
# pythonDict = json.loads(jsonString)

# # el resultado
# print(pythonDict["city"])


"""
podemos transformar un objeto python a un json con el metodo
json.dumps()
"""
# # a Python object (dict):
# x = {"name": "John", "age": 30, "city": "New York"}

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)
# print(type(y))

"""
lista de objetos python que se puede transformar en un json

dict
list
tuple
string
int
float
True
False
None
"""

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

"""
https://www.w3schools.com/python/python_json.asp

"""

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

# print(json.dumps(x))

"""
el metodo dump puede tener cierto formato dependiendo de como querramos ver el
json al final
"""
# print(json.dumps(x, indent=4))

# print(json.dumps(x, indent=4, separators=(". ", " :: ")))

print(json.dumps(x, indent=4, sort_keys=True))
