import unittest
import mysql.connector
from person import Person
from datetime import date, timedelta, datetime

class Hotel(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="hotel"
        )

    def dbase(self):
        cursor = self.mydb.cursor()
        cursor.execute("select * from Room")

        results = cursor.fetchall()
        for record in results:
            print(record)
    
    def check_in(s  elf, person, room_type, checkin_date=None):
        if not checkin_date:
            checkin_date = datetime.now()
        
        cursor = self.mydb.cursor()
        cursor.execute("select id, total from Room where room_type=%s", [room_type])
        record = cursor.fetchone()
        room_id = record[0]
        room_type_total = record[1]

        cursor.execute("""
            select count(*) as total  from Guest 
            where Guest.room_id = %s
        """, [room_id])
        used_rooms = cursor.fetchone()[0]

        if room_type_total <= used_rooms:
            raise Exception("The hotel is full")

        cursor.execute("""
            Insert into Person
                (last_name, first_name, ssn)
                VALUES (%s, %s, %s)
        """, [person.name, person.last_name, person.ssn])

        person_id = cursor.lastrowid

        cursor.execute("""
            Insert into Guest
                (person_id, check_in, room_id)
                VALUES (%s, %s, %s)
        """, [person_id, checkin_date, room_id])
        self.mydb.commit()

        return cursor.lastrowid

    def check_out(self, reservation_id, checkout_date=None):         
        if not checkout_date:
            checkout_date = datetime.now()
            
        cursor = self.mydb.cursor()
        
        cursor.execute("""
                Select room_price, check_in from Room join Guest 
                on Guest.room_id = Room.id 
                where Guest.id = %s""", [reservation_id])
        record = cursor.fetchone()
        room_price = record[0]
        check_in = record[1]

        total_days = (checkout_date - check_in).seconds

        cursor.execute("""
                UPDATE Guest SET check_out = %s
                where Guest.id = %s
            """, [checkout_date, reservation_id])
        self.mydb.commit() 
     
        return total_days * room_price

class TestHotel(unittest.TestCase):
    def test_check_in(self):
        hotel1 = Hotel({'single':15, 'double':30, 'suite':45}, {'single':10, 'double':20, 'suite':30}) 
        
        guest1_id = 1
        guest2_id = 2

        person1 = Person(guest1_id, "Amarilis")
        person2 = Person(guest2_id, "Javier")

        d1 = date(2022, 5, 10)
        d2 = date(2022, 5, 12)

        hotel1.check_in(person1, "single", d1 )
        hotel1.check_in(person2, "single", d2 )

        assert hotel1.room_types_count["single"] - hotel1.reserved_room["single"] == 8
        assert hotel1.guest_state[guest1_id][0] == "Amarilis"
        assert hotel1.guest_state[guest1_id][1] == "single"
        assert hotel1.guest_state[guest1_id][2] == d1
        
        
        # if hotel1.guest_state[1]= 8:
        #     raise Error("not correct")

        #self.guest_state[person.id] = [person.name, room_type, date]
        
    def test_check_out(self):
        
        hotel1 = Hotel({'single':15, 'double':30, 'suite':45}, {'single':10, 'double':20, 'suite':30}) 
        
        guest1_id = 1
        person1 = Person(guest1_id, "Amarilis")
        check_in_1 = date(2022, 5, 10)
        check_out_1 = date(2022, 5, 15)

        hotel1.check_in(person1, "single", check_in_1 )
        assert (check_out_1 - hotel1.guest_state[guest1_id][2]).days == 5
        
        total_price = hotel1.check_out(guest1_id, check_out_1)

        assert total_price == 75
     
hotel1 = Hotel()

while True:
    action = int(input("Do you want to check_in(1) or check_out(2): "))

    if action == 1:
        name = input("Enter first name: ")
        last = input("Enter last name: ")
        ssn = input("Enter SSN: ")
        room_type = input("Enter what room do you want: ")

        print("Checkin in that person")
        reservation_id = hotel1.check_in(Person(1, name, last, ssn), room_type) 

        print("Welcome to the Hotel. Your reservation Id is: " + str(reservation_id))
    else:
        reservation_id = input("Enter your reservation id: ")
        price  = hotel1.check_out(reservation_id)

        print("the total price is:" + str(price))

        

# if __name__ == '__main__':
#     unittest.main()
