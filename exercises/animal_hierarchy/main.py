from animal import Animal
from falcon import Falcon
from air_animal import Air_Animal
from elephant import Elephant
from bee import Bee
from cocodrile import Cocodrile


animal_list = [
    Elephant("Pepe", 20, "Africano"),
    Falcon("Deu", 56, "Ingles"),
    Bee("Roro", 45, "Worked"), 
    Cocodrile("Tito", 4, "Cuban")
]

for animal in animal_list:
    print(animal.name)
    animal.move()

    if isinstance(animal, Air_Animal):
        print(animal.wing_count)
