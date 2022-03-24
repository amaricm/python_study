
class Property:
    def __init__(self, owner_id, number_of_rooms, number_of_bathrooms, sqft, lote, price, street, city, zip_code, realtor_id, year_of_construction, status, create_date=None, id=0):
        self.__id=id
        self.owner_id=owner_id
        self.number_of_rooms=number_of_rooms
        self.number_of_bathrooms=number_of_bathrooms
        self.sqft=sqft
        self.lote=lote
        self.price=price
        self.street=street
        self.city=city
        self.zip_code=zip_code
        self.create_date=create_date
        self.realtor_id=realtor_id
        self.year_of_construction=year_of_construction
        self.status=status

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id
