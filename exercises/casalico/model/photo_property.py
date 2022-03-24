class Photos_Property:
    def __init__(self,id,property_id,image_path):
        self.__id=id
        self.property_id=property_id
        self.image_path=image_path         

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id