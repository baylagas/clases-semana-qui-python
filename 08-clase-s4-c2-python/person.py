# la clase person
# a esta clase le creamos el metodo constructor __init__()
# que recibe 2 parametros el nombre y la edad
# este metodo crea dos variables de instancia llamadas name y age
"""
clases en base a sus propiedades y acciones
"""


"""
hay clases que solo tienen propiedades (variables)
    su proposito es solo guardar informacion

ejercicio: coloquele el dui
"""


class Person:
    # metodo constructor de la clase
    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
hay clases que solo tiene acciones (metodos)
    su proposito es solo procesar informacion, otras clases, clases trabajadoras

ejercicio: coloquele un metodo createBoat() print creating boat
"""


class Factory:
    def createCar(self):
        print("creating car...")

    def createComputer(self):
        pass

    def createAirplane(self):
        pass


"""
hay clases mas comunes que tienen ambos= guardan informacion y tienen metodos que procesan
    esa informacion

ejercicio: agregarle number3, agregarlo a todos metodos y agregar un metodo mas que de el average
"""


class Operation:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def multiply(self):
        return self.number1 * self.number2
