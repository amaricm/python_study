from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, tag):
        super().__init__(tag, "truck")