# from <archivo py> import <clase, metodo, variable>
from person import Person, Factory, Operation


person1 = Person("balbino", 23)
# print(person1)
print(person1.name)
print(person1.age)

factory1 = Factory()
factory1.createCar()

operation1 = Operation(2, 4)
result = operation1.add()
print(result)
result = operation1.multiply()
print(result)
