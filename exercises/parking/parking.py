from vehicle import Vehicle
from truck import Truck
from car import Car
from motorcycle import Motorcycle
from datetime import datetime


class Parking(object):
    def __init__(self, prices, limit, accepted_vehicles):
        self.prices = prices
        self.limit = limit
        self.accepted_vehicles = accepted_vehicles
        self.vehicle_count = 0
        self.parking_state = {}
  

    def can_enter(self, vehicle):
        return vehicle.type in self.accepted_vehicles

    def is_full(self):
        return self.limit == self.vehicle_count
    
    def park_vehicle(self, vehicle, date=datetime.now()):
        if self.is_full():
             raise Exception("Parking is Full")
        if not self.can_enter(vehicle): 
            raise Exception("This type of vehicle is not permitted")
        
        self.vehicle_count += 1
        self.parking_state[vehicle] = date
    
    def exit_vehicle(self, vehicle):
        time_now = datetime.now()
        diff = time_now - self.parking_state[vehicle]    
        total_hours = int(diff.total_seconds() / 3600)
        self.vehicle_count -= 1
        return self.prices[vehicle.type] * total_hours
       
        
        









    # def vehicle_entrance(self, vehicle, date):
    #     if self.can_enter(vehicle): 
    #         self.vehicle_count += 1
    #         self.prices[vehicle] = datetime.now

    # def vehicle_exit(self, prices):
    #     if 

   
              





       

        

       