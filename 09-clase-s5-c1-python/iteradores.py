# iteradores

studentList = ["balbino", "rodrigo", "david"]
# for student in studentList:
#     print(student)

word = "hola"
# for letter in word:
#     print(letter)

# un iterador es un objeto que contiene un numero contable de valores
# es que debe de poder iterar sus valores, llegar a cada uno

# para que un objeto pueda ser un iterador debe implementar el protocolo
# de python para iteradores, que consiste en utilizar dos metodos
#  __iter__() y el metodo __next__()

studentTuple = ("balbino", "rodrigo", "david", "luna", "patricia")

# for student in studentTuple:
#     print(student)

# iterator = iter(studentTuple)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for student in iter(studentTuple):
#     print(student)

# como puedo crear yo un iterador?
# 1. deben crear una clase que implemente los metodos __iter__() y __next__()


# class MyNumbers:
#     # implementarcion de iter
#     def __iter__(self):
#         self.a = 1
#         return self

#     # implementacion del metodo next
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x


# myclass = MyNumbers()
# iterador = iter(myclass)

# print(next(iterador))
# print(next(iterador))
# print(next(iterador))


# class MyNumbers:
#     # implementarcion de iter
#     def __iter__(self):
#         self.contador = 1
#         return self

#     # implementacion del metodo next
#     def __next__(self):
#         if self.contador <= 20:
#             numero = self.contador
#             self.contador += 1
#             return numero
#         else:
#             raise StopIteration


# myclass = MyNumbers()
# iterador = iter(myclass)

# for number in iterador:
#     print(number)


class MyNumbers:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    # implementarcion de iter
    def __iter__(self):
        self.contador = self.start
        return self

    # implementacion del metodo next
    def __next__(self):
        if self.contador <= self.finish:
            numero = self.contador
            self.contador += 1
            return numero
        else:
            raise StopIteration


myclass = MyNumbers(10, 100)
iterador = iter(myclass)

for number in iterador:
    print(number)

"""
ejercicio de la creacion de un iterador
colocarle un step
myclass = MyNumbers(4, 10 , 2)
output
4
6
8
10
"""
