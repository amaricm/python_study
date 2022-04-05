from land_animal import Land_Animal

class Mammal(Land_Animal):
    def __init__(self, leg_count, name, age, sub_specie):
        super().__init__(leg_count, name, age, sub_specie)     

