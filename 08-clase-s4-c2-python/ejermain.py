from ejerperson import Person
from ejerjobhelper import JobHelper

personList = []

personList.append(Person("rodrigo", 18))
personList.append(Person("marta", 24))
personList.append(Person("alexia", 50))
personList.append(Person("gabriela", 48))
personList.append(Person("guillermo", 30))

personList.append(Person("rodolfo", 27))
personList.append(Person("fernando", 38))
personList.append(Person("griselda", 55))
personList.append(Person("tamara", 19))
personList.append(Person("pepito", 21))


# variable tiene un objeto (instancia) de clase JobHelper
jobHelper1 = JobHelper()
rangeDict = jobHelper1.organizePersonByRange(personList)

print(rangeDict)
rangeACount = len(rangeDict["rangeA"])
print(f"range A count {rangeACount}")
for person in rangeDict["rangeA"]:
    print(person.name)
rangeBCount = len(rangeDict["rangeB"])
print(f"range B count {rangeBCount}")
for person in rangeDict["rangeB"]:
    print(person.name)


# def metodo(personList):
#     for person in personList:
#         print(person.name)


# metodo(personList)
