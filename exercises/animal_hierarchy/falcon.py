from bird import Bird

class Falcon(Bird):
    def __init__(self, name, age, sub_specie):
        super().__init__(name, age, sub_specie)

    def sleep(self):
        print("I sleep like an Falcon")

    def eat(self):
        print("I eat like an Falcon")        

    def fly(self):
        print("I fly like an Falcon with my %s wings" % self.wing_count)  

    
