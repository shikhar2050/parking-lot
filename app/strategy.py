from app.enums import SizeEnum
from abc import ABC, abstractmethod


class ParkingStrategy(ABC):
    @abstractmethod
    def park(self, vehicle, spots):
        pass


class FirstSpotStrategy(ParkingStrategy):
    def park(self, vehicle, floors):
        for floor in floors:
            for spot in floor.get_spots():
                if spot.is_free():
                    if vehicle.get_size() == SizeEnum.COMPACT and spot.get_size() in [SizeEnum.COMPACT, SizeEnum.LARGE, SizeEnum.XL]:
                        return spot
                    elif vehicle.get_size() == SizeEnum.LARGE and spot.get_size() in [SizeEnum.LARGE, SizeEnum.XL]:
                        return spot
                    elif vehicle.get_size() == SizeEnum.XL and spot.get_size() in [SizeEnum.XL]:
                        return spot
        return None


class EfficientSpotStrategy(ParkingStrategy):
    def park(self, vehicle, floors):
        for floor in floors:
            return EfficientSpotStrategy.search_spot_by_type(vehicle.get, floor.get_spots())

    @staticmethod
    def search_spot_by_type(vehicle_size, spots):
        if not vehicle_size:
            return None

        for spot in spots:
            if vehicle_size == spot.get_size():
                return spot

        return EfficientSpotStrategy.search_spot_by_type(EfficientSpotStrategy.find_next_big(vehicle_size), spots)

    @staticmethod
    def find_next_big(vehicle_type):
        if vehicle_type == SizeEnum.COMPACT:
            return SizeEnum.LARGE
        elif vehicle_type == SizeEnum.LARGE:
            return SizeEnum.XL
        else:
            return None
