# herencia

# herencia en la vida real
# - herencia de bienes fisicos o monetarios
# - genetica = rasgos fisicos, mentales de padres a hijos

# Clase
class Person:
    def __init__(self, name, hairColor, haveTatoo, eyeColor):
        self.name = name
        self.hairColor = hairColor
        self.haveTatoo = haveTatoo
        self.eyeColor = eyeColor

    def sendMessage(self, message):
        print(f"Person: {message}")


person1 = Person("balbino", "black", False, "brown")

# herencia en programacion
# la herencia nos permite definir clases que herendan todos los metodos y propiedades
# de otras clases

# sin herencia
# class Student:
#     def __init__(self, name, hairColor):
#         self.name = name
#         self.hairColor = hairColor


# student1 = Student("pepito", "azul")

# con herencia
# una clase padre y una clase hija
# la clase padre es Person y la clase hija sera Student


# class Student(Person):
#     pass


# class Student(Person):
#     def __init__(self, name, hairColor, haveTatoo):
#         Person.__init__(self, name, hairColor, haveTatoo)


class Student(Person):
    def __init__(self, name, hairColor, haveTatoo, eyeColor, learningInstitute):
        super().__init__(name, hairColor, haveTatoo, eyeColor)
        self.learningInstitute = learningInstitute

    def singAnthem(self):
        print("sing countries anthem")

    def sendMessage(self, message):
        print(f"Student: {message}")

    def sendMessagePerson(self, message):
        super().sendMessage(message)


student1 = Student("pepito", "celeste", True, "blue", "la escuelita")
print(student1.name)
print(student1.hairColor)
print(student1.haveTatoo)
print(student1.eyeColor)
print(student1.learningInstitute)
student1.sendMessage("hola soy un estudiante")
student1.sendMessagePerson("uhhhh este es otro mensaje")
student1.singAnthem()

# genaral
#   automovil (4 llanta, un motor, 2 puertas, baul)
#   sedan caminota
#   toyota, chevrolet, ferrari
#                suburban    f8 spider
# especifico

# dentro de un student hay person
