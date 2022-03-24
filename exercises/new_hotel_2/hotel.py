import unittest
from person import Person
from datetime import date, timedelta


class Hotel(object):
    def __init__(self, room_prices, room_types_count):
        self.room_prices = room_prices
        self.room_types_count = room_types_count
        self.guest_state = {}    
        
    def check_in(self, person, room_type, checkin_date, checkout_date):
        if self.availability(checkin_date, checkout_date):
            self.guest_state[person.id] = [person.name, room_type, checkin_date, checkout_date]

    def availability(self, checkin_date, checkout_date):
        delta = (checkout_date - checkin_date).days
        for day in range(0, delta):
            check_day = checkin_date + timedelta(days=day)
            day_room_count = 0

            for person_id,person_data in self.guest_state.items():
                guest_checkin_date = person_data[2]
                guest_checkout_date = person_data[3]
                




      