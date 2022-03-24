class User:
    def __init__(self,id,name,last_name,email, phone, user_type, login=None, password=None):
        self.__id=id
        self.name=name
        self.last_name=last_name
        self.email=email
        self.phone=phone
        self.user_type = user_type
        self.login = login
        self.password = password

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id