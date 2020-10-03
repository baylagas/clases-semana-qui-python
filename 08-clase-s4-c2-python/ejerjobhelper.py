class JobHelper:
    def organizePersonByRange(self, personList):
        # 1.crear un elemento range Dictionary
        aRangeDict = self.createRangeDict()
        # 2.luego vamos a organizar la informacion de personlist en el
        # range dictionary
        for person in personList:
            if 16 <= person.age <= 35:
                aRangeDict["rangeA"].append(person)
            elif 36 <= person.age <= 65:
                aRangeDict["rangeB"].append(person)
        return aRangeDict

    def createRangeDict(self):
        rangeDict = {}
        # rangeA 16 a 35
        rangeDict["rangeA"] = []  # lista mas peque con personas que aplique la edad
        # rangeA 36 a 65
        rangeDict["rangeB"] = []  # lista mas peque con personas que aplique la edad
        return rangeDict
