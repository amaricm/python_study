class Animal(object):
    def __init__(self, number_of_leg, age):
        self.number_of_eyes = 2
        self.heart = 1
        self.numer_of_legs = number_of_leg
        self.age = age

    def walk(self,direction, number_of_steps):
        print(f"I walked {number_of_steps} steps with my {self.number_of_leg} to {direction} ")

    def birthday(self):
        self.age += 1
        if self.age > 20:
            raise Exception("Animal died")

    def make_sound(self, intensity):
        raise Exception("I am an animal, I am abstract")
        
class Duck(Animal):
    def __init__(self, feather_color, age):
        self.feather_color = feather_color
        super().__init__(2, age)

    def make_sound(self, intensity):
        print(f"I QUAK {intensity}")

    def quak(self,intensity):
        print(f"I quak {intensity} and I am {self.age} year old")    

class Dog(Animal):
    
    def __init__(self, hair_color, age):
        self.hair_color = hair_color
        super().__init__(4, age)

    def bark(self,intensity):
        print(f"I bark {intensity} and I am {self.age} year old")

    def make_sound(self, intensity):
        print(f"I BARK {intensity}")    
        

animals = [Dog("brown", 3), Duck("yellow", 5) ]

for animal in animals:
    animal.make_sound("low")

# for x in animals:
#     if isinstance(x, Dog):
#         # print(x.age)
#         x.bark("high")
#     elif isinstance(x, Duck):
#         x.quak("low")

# print(isinstance(animal, Dog))
# print(isinstance(animal, Duck))
# print(isinstance(animal, Animal))


# dog_1.birthday()      
# dog_1.age = 70

# dog_1.bark("Very High")      
# duck_1.quak("high")
# print(f"Dog1 with hair color: {dog_1.hair_color} have {dog_1.age} years")

# print(f"Duck1 with feather color: {duck_1.feather_color} have {duck_1.age} years")
