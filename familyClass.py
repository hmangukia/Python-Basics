class Family:

    def __init__(self, father, mother, son, daughter):
        self.father = father
        self.mother = mother
        self.son    = son
        self.daughter = daughter

    def pray(self):
        print("Mr {}'s Family is Praying".format(self.father))

    def haveFun(self):
        print("Mr {}'s Family is now having fun...".format(self.father))

    def getFather(self):
        print("I am Mr {}, the father of the house".format(self.father))

    def getMother(self):
        print("I am Mrs {}, the mother of the house".format(self.mother))

    def getSon(self):
        print("I am Master {}, the man of the house".format(self.son))

    def getDaughter(self):
        print("I am Miss {}, the lady of the house".format(self.daughter))


        
        
def main():
    newFamily = Family("Kelvin", "Rose", "Prince", "Gwachi")

    newFamily.pray()

    newFamily.haveFun()

    newFamily.getFather()

    newFamily.getMother()

    newFamily.getSon()

    newFamily.getDaughter()

main()
    
