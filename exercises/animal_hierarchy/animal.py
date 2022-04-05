from abc import abstractmethod

class Animal(object):
    def __init__(self, name, age, sub_specie):
        if age < 0:
            raise Exception("age must be positive number")
        self.name = name 
        self.age = age 
        self.sub_specie = sub_specie  

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass        
    
    @abstractmethod
    def move(self):
        pass