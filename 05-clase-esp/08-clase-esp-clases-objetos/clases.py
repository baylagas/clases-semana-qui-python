# clases - objetos

# clase
# nos permitira poder modelar un objeto de la vida real de forma digital

# definicion de la clase
# class MyClass:
#     # variables de clase
#     x = 5


# clase Persona
# class Person:
#     name = "balbino"


# como llamar una clase, como crear un objeto(instancia) de una clase
# v1 = MyClass()
# print(type(v1))
# print(v1)
# print(v1.x)

# person1 = Person()
# print(type(person1))
# print(person1)
# print(person1.name)

# el metodo constructor de una clase
# en python se ocupa el metodo __init__() para inicializar la clase para ser utilizada


# class Person:
#     def __init__(self, name):
#         self.name = name


# person1 = Person("fatima")
# print(person1.name)

# que pasaria si quiero agregar una variable para la edad
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# person1 = Person("balbino", 24)
# print(person1.name)
# print(person1.name, person1.age)

# como crear metodos para un clase
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # crear el metodo talk()
#     def talk(self, message):
#         print("me: " + message)


# person1 = Person("rodrigo", 43)
# print(person1.name)
# print(person1.name, person1.age)
# person1.talk("que buen dia fue ayer")

# parametro self
# self es una referencia a la actual instancia de esa clase, es usado para accedes a variables
# que estan dentro de la clase
# ahora algo interesante es que realmente no es necesario que sea siempre self, puede llamarse
# cualquier cosa por ejemplo pepito pero debe ser el primer valor del init()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # crear el metodo talk()
#     def talk(self, message):
#         print("me: " + message)


# person1 = Person("rodrigo", 43)
# print(person1.name)
# print(person1.name, person1.age)
# person1.talk("que buen dia fue ayer")

# como podemos modificar la instancia de una clase
# person1 = Person("marcela", 25)
# person1.age = 26
# print(person1.name, person1.age)

# se puede eliminar variables por medio del "del"
# del person1.name
# # print(person1.name, person1.age)
# print(person1.age)


# podemos eliminar variables completas por medio de del
# del person1
# print(person1)

# la palabra reservada pass


# class Personal:
#     pass
