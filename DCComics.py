
class DCComics:
    def __init__(self, name, born, weapon, bestactorname):
        self.__name = name
        self.__born = born
        self.__weapons = list(weapon)
        self.__bestactorname = bestactorname

    def __str__(self):
        return f"My name is {self.__name}, I was bor in {self.__born} and I fight using {self.__weapons}, I was played by {self.__bestactorname}."

    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def setborn(self,born):
        self.__born = born

    def getborn(self):
        return self.__born

    def addweapon(self, weapon):
        self.__weapons.append(weapon)

    def removeweapon(self, weapon):
        self.__weapons.remove(weapon)

    def getweapons(self):
        return self.__weapons

    def setbestactorname(self,bestactorname):
        self.__bestactorname = bestactorname

    def getbestactorname(self):
        return self.__bestactorname

monkey = DCComics("Idiot", 2000, ["poop"], "Gorila")
print (monkey.__str__())
print (monkey.getborn())

a = DCComics("Ivan", 1926, ["gun"], "DICaprio")
print(a.getname())
a.setname("Igor")
print(a.getname())

b = DCComics("Terrorist", 1969, ["sword"], "someone")
print(b.__str__())
print (b.getweapons())
b.addweapon("shield")
print (b.getweapons())