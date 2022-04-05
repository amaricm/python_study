from animal import Animal
from land_animal import Land_Animal
from reptile import Reptile

class Cocodrile(Reptile):
    def __init__(self, name, age, sub_specie):
        super().__init__(4, name, age, sub_specie)

       
    def sleep(self):
        print("I sleep like an Cocodrile")

    def eat(self):
        print("I eat like an Cocodrile")        

    def walk(self):
        print("I walk like an Cocodrile with my %s legs" % self.leg_count)  