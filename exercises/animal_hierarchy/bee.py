from air_animal import Air_Animal

class Bee(Air_Animal):
    def __init__(self, name, age, sub_specie):
        super().__init__(2, name, age, sub_specie)

    def sleep(self):
        print("I sleep like an Bee")

    def eat(self):
        print("I eat like an Bee")        

    def fly(self):
        print("I fly like an Bee with my %s wings" % self.wing_count)  

