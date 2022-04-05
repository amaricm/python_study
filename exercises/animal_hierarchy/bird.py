from animal import Animal
from air_animal import Air_Animal

class Bird(Air_Animal):
    def __init__(self, name, age, sub_specie):
        super().__init__( 2, name, age, sub_specie)
