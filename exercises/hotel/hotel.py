
from room import Room
from person import Person
from datetime import datetime, timedelta


class Hotel(object):
    def __init__(self, room_list):
        self.guess_state = {}
        self.room_count = {}
        self.room_list = room_list
              

    
        

    def find_room_type_in_list(self, room_type): 
        for room in self.room_list.keys():
            if room == room_type:
                return True



   def check_in(self, person, room_type, date=datetime.now()):
        if find_room_type_in_list(room_type): 
            



    def find_if_available(self, room_type):


         
       

    def is_full(self):
        return room.quantity == self.room1_count
        self.guess_state[person] = [room, date]
       
