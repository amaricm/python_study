from abc import abstractmethod
from bicicle import Bicicle


class Carbon_Fiber_Bici(Bicicle):
    def __init__(self, brand, color, day_of_manufacture):
        super().__init__(brand, color, day_of_manufacture, 2)


    def run(self):
        print("I run like a Carbon Fiber bici with my %s weels" % self.number_of_wheel)
    
    def beep(self):
        print("I beep like a Carbon Fiber bici")

    def park(self):
        print("I park like a Carbon Fiber bici")