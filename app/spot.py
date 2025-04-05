from app.enums import SizeEnum
from abc import ABC, abstractmethod


class ParkingSpot(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.occupied = False
        self.vehicle = None

    def get_size(self):
        return self.size

    def is_free(self):
        return not self.occupied

    def occupy(self, vehicle):
        self.occupied = True
        self.vehicle = vehicle

    def free(self):
        self.occupied = False
        self.vehicle = None

    def __str__(self):
        return f"({self.name} {self.occupied}, {self.size})"

    def __repr__(self):
        return f"({self.name} {self.occupied}, {self.size})"


class CompactSpot(ParkingSpot):
    def __init__(self, name):
        super().__init__(name, SizeEnum.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, name):
        super().__init__(name, SizeEnum.LARGE)


class XLSpot(ParkingSpot):
    def __init__(self, name):
        super().__init__(name, SizeEnum.XL)


class ParkingFloor:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def get_spots(self):
        return self.spots

    def __repr__(self):
        return self.name
