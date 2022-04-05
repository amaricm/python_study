from abc import abstractmethod

class Transport(object):
    def __init__(self, brand, color, day_of_manufacture):
        self.brand = brand
        self.color = color 
        self.day_of_manufacture = day_of_manufacture


    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def beep(self):
        pass

    @abstractmethod
    def park(self):
        pass