from animal import Animal
from air_animal import Air_Animal

class Insect(Reptile):
    def __init__(self, wing_count, name, age, sub_specie):
        self.wing_count = wing_count
        super().__init__(name, age, sub_specie)

