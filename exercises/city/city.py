from house import House
from person import Person

class City(object):
    def __init__(self, name, city_area):
        self.name = name
        self.city_area = city_area
        self.person = {}
        self.house = {}
        total_area = 0

    def person_registry(self, person):
        self.person[person.id] = person

    def house_registry(self, house):
        self.house[house.id] = house

    def report_race(self, race):
        race_count = 0
        for person_instance in self.person.values():
            if race == person_instance.race:
                race_count = race_count + 1
        return race_count

    def report_sex(self, sex):
        sex_count = 0
        for person_instance in self.person.values():
            if sex == person_instance.sex:
                sex_count = sex_count + 1
        return sex_count

    def tax_calculator(self, house_id):
        return self.house[house_id].area * 3
    
    def total_house(self):
        return  len(self.house.keys())

    def total_area(self):
        total_area = 0
        for house in self.house.values():
            total_area = house.area + total_area 
        return total_area
   
    def new_house_capacity(self, city_area, new_home_area):
        if city_area - self.total_area() > new_home.area:
            return True
        return False
   



           

