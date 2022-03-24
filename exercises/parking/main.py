import time
from parking import Parking
from vehicle import Vehicle
from truck import Truck
from car import Car
from motorcycle import Motorcycle
from datetime import datetime, timedelta


parking = Parking({"car": 5, "moto": 2}, 10, ["car", "moto"])
 
car_1 = Car("Hsr19")
car_2 = Car("H2039")

date_car_1 = datetime.now() - timedelta(hours=5)
date_car_2 = datetime.now() - timedelta(hours=3)

parking.park_vehicle(car_1, date_car_1)
parking.park_vehicle(car_2, date_car_2)

for car, date  in parking.parking_state.items():
    str_date = date.strftime("%b %d %Y %H:%M:%S")
    print(f"tag:{car.tag} - date:{str_date}")


print(parking(car_1))


print(parking.exit_vehicle)
print(parking.exit_vehicle(car_2))

