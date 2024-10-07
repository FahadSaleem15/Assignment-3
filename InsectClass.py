import random

class insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0
        self.name = name

    def calc_flight(self):
        self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight
    
    def get_name(self):
        return self.name