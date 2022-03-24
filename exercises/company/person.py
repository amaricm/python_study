class Person:
    def __init__(self,id,name,last_name,email):
        self.__id=id
        self.name=name
        self.last_name=last_name
        self.email=email

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id