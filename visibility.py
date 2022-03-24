class Store:
    
    def __init__(self):
        self.__coef = 25

    def get_price(self, product_cost):
        return product_cost + (self.__coef/100)*product_cost

    def get_coef(self):
        return self.__coef

store = Store()
print("we are adding a %s coef to product prices" % store.get_coef())
print(store.get_price(40))