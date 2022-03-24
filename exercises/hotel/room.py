class HotelRoom(object):
    def __init__(self, type, price, quantity):
        self.__type = type
        self.__price = price
        self.__quantity = quantity

    def  get_type(self):
        return self.__type

    def  get_price(self):
        return self.__price

    def  get_quantity(self):
        return self.__quantity





# single = Room("single", 20)

# double_room = Room("double", 40)

# suite = Room("suite", 80)


# class Dog(object):

#     def __init__(self, hair_color, age):
#         self.hair_color = hair_color
#         self.age = age


dali = Dog("brown", 8)

pacho = Dog("black", 10)

lola = Dog("white", 3)