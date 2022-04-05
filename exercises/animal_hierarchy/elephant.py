from mammal import Mammal

class Elephant(Mammal):
    def __init__(self, name, age, sub_specie):
        self.pepe = "jose"
        super().__init__(4, name, age, sub_specie)
            
    def sleep(self):
        print("I sleep like an Elephant")

    def eat(self):
        print("I eat like an Elephant")        

    def walk(self):
        print("I walk like an Elephant with my %s legs" % self.leg_count)    