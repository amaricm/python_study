from animal import Animal
from abc import abstractmethod

class Air_Animal(Animal):
    def __init__(self, wing_count, name, age, sub_specie):
        self.wing_count = wing_count
        super().__init__(name, age, sub_specie)

    @abstractmethod
    def fly(self):
        pass

    def move(self):
        self.fly()
