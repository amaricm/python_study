
class Company:
    def __init__(self, id,name,cash, registry_date=None):
        self.__id=id
        self.name=name
        self.cash=cash
        self.registry_date=registry_date
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

