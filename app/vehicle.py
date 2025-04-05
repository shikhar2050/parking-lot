from app.enums import SizeEnum
from abc import ABC, abstractmethod
from app.ticket import ParkingTicket


class Vehicle(ABC):
    def __init__(self, size: SizeEnum):
        self.size = size
        self.ticket = None

    def assign_ticket(self, ticket: ParkingTicket):
        self.ticket = ticket

    def get_ticket(self) -> ParkingTicket:
        return self.ticket

    def get_size(self) -> SizeEnum:
        return self.size

    def __str__(self):
        return self.__class__.__name__


class Bike(Vehicle):
    def __init__(self):
        super().__init__(SizeEnum.COMPACT)


class Truck(Vehicle):
    def __init__(self):
        super().__init__(SizeEnum.XL)


class Car(Vehicle):
    def __init__(self):
        super().__init__(SizeEnum.LARGE)


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == 'Bike':
            return Bike()
        elif vehicle_type == 'Truck':
            return Truck()
        else:
            return Car()
