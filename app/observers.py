from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, floor):
        self.floor = floor

    def get_floor(self):
        return self.floor

    @abstractmethod
    def update(self, spots):
        pass

    @staticmethod
    def show_message(message):
        print(message)


class ParkingDisplayBoard(Observer):
    def update(self, spots):
        print(f"Updating Latest spots in {self.floor}")

