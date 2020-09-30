# clases y objetos

# que es una clase
# definicion de la clase
class Mensaje:
    x = 5


class Person:
    name = "balbino"
    age = 23
    salary = 350.5


objeto = Mensaje()

print(type(objeto))
print(objeto)
print(objeto.x)

objeto = Person()
print(type(objeto))
print(objeto)
print(f"{objeto.name} ++ {objeto.age} ++ {objeto.salary:.2f}")
objeto.name = "claudia"
objeto.age = 42
print(f"{objeto.name} ++ {objeto.age} ++ {objeto.salary:.2f}")