"""
Scope dentro de python

una variable esta disponible solamente en la region en la que es creada, y esto
es lo que conocemos como scope

"""

"""
local scope
una variable es creada dentro de una funcion y se dice que esa variable en esta
dentro del scope de esa funcion y solo puede ser usada dentro de esa funcion
"""


# def myfunc():
#     number = 300
#     print(number)


# myfunc()


"""
en python podemo crear funciones dentro de otras funciones
dentro del scope de una funcion podemos crear otras

"""


# def myfunc():
#     number = 250

#     def myInnerFunc(newNumber):
#         newNumber = newNumber * 2
#         print(number)
#         print(newNumber)

#     myInnerFunc(number)


# myfunc()

"""
global scope
una variable creada en el cuerpo principal del codigo python es una variable global
y funciona en un global scope
las variable en un global scope pueden ser utilizadas dentro de cualquiera de los
scopes anteriores (local y global)
"""
# number = 300


# def myfunction():
#     print(number)


# myfunction()
# print(number)

"""
nombres de variables en distintos scopes
si uno utiliza un nombre de variable similar dentro y afuera de una funcion, python
va a tratar a ambas variables como distintas, una estara disponible en un global scope
y la otra esta disponible en un local scope
"""

# number = 300


# def myfunction():
#     number = 200
#     print(number)


# myfunction()
# print(number)

"""
la palabra reservada global
esta palabra reservada nos ayuda cuando queremos que una variable creada en un local scope
pueda ser utilizada en un global scope
"""


def myfunc():
    global number
    number = 150


myfunc()
print(number)
