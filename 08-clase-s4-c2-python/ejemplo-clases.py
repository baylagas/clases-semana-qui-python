# from <archivo py> import <clase, metodo, variable>
from person import Person, Factory, Operation


person1 = Person("balbino", 23, 100)
# print(person1)
print(person1.name)
print(person1.age)
print(person1.id)

factory1 = Factory()
factory1.createCar()
factory1.createBoat()

operation1 = Operation(2, 4, 10)
result = operation1.add()
print(result)
result = operation1.multiply()
print(result)
result = operation1.average()
print(f"{result:.2f}")
