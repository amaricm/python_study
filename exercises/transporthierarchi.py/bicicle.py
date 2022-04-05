from transport import Transport
from abc import abstractmethod

class Bicicle(Transport):
    def __init__(self, brand, color, day_of_manufacture, number_of_wheel):
        self.number_of_wheel = 2
        super().__init__(brand, color, day_of_manufacture)

