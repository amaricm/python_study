from vehicle import Vehicle

class Car(Vehicle):
     def __init__(self, tag):
        super().__init__(tag, "car")
   