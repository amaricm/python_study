from animal import Animal
from abc import abstractmethod

class Land_Animal(Animal):
    def __init__(self, leg_count, name, age, sub_specie):
        self.leg_count = leg_count
        super().__init__(name, age, sub_specie)

    @abstractmethod
    def walk(self):
        pass

    def move(self):
        self.walk()