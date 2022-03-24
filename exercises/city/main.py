import unittest
from city import City
from house import House
from person import Person

class TestHotel(unittest.TestCase):

    def test_person_registry(self):

        person1 = Person(1, "Amarilis", 30, "white", "F")
        person2 = Person(2, "Javier", 40, "white", "M")   

        city1 = City("Miami", 300)

        city1.person_registry(person1)
        city1.person_registry(person2)

        assert  city1.person[person1.id] == person1

    def test_house_registry(self):
        
        house1 = House(1,)


if __name__ == '__main__':
    unittest.main()
