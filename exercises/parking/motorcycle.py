from vehicle import Vehicle

class Motorcycle(Vehicle):
   def __init__(self, tag):
        super().__init__(tag, "motorcycle")