import datetime
import math
from abc import ABC, abstractmethod


class ParkingTicket:

    def __init__(self, entry_gate, spot):
        self.ticket_id = self.generate_parking_id()
        self.issued_at = datetime.datetime.now()
        self.status = ParkingTicketCreatedState()
        self.rate = ParkingTicketRate()
        self.spot = spot
        self.charge = 0
        self.entry_gate = entry_gate
        self.exit_gate = None

    @staticmethod
    def generate_parking_id():
        return TicketId().get_ticket_id()

    def print_ticket(self):
        for key, value in self.__dict__.items():
            print(f"\033[94m{key}\033[0m: {value}")

    def promote(self, exit_gate=None):
        if self.status == ParkingTicketPaidState:
            self.exit_gate = exit_gate
        self.status = self.status.promote()
        print(f"Ticket {self.ticket_id} is promoted to {self.status}")

    def close(self, exit_gate=None):
        if self.status.__class__ != ParkingTicketPaidState:
            return False

        self.status.promote()
        self.exit_gate = exit_gate
        self.spot.free()

        self.promote()

    def calculate_charge(self):
        exit_time = datetime.datetime.now()
        duration = math.ceil((exit_time - self.issued_at).total_seconds())
        return self.rate.calculate_total_fee(duration)


class ParkingTicketRate:
    def __init__(self):
        self.rate = 20
        self.period = 1

    def set_rate(self, rate):
        self.rate = rate

    def set_period(self, period):
        self.period = period

    def calculate_total_fee(self, duration):
        return self.rate * math.ceil(duration / self.period)

    def __repr__(self):
        return self.rate.__str__()


class TicketId:
    _ID = 0

    def __init__(self):
        TicketId._ID += 1

    def get_ticket_id(self):
        return self._ID


class ParkingTicketState(ABC):
    @abstractmethod
    def promote(self):
        pass

    def __repr__(self):
        return self.__class__.__name__[13:-5]


class ParkingTicketCreatedState(ParkingTicketState):
    def promote(self):
        return ParkingTicketActiveState()


class ParkingTicketActiveState(ParkingTicketState):
    def promote(self):
        return ParkingTicketPaidState()


class ParkingTicketPaidState(ParkingTicketState):
    def promote(self):
        return ParkingTicketExpiredState()


class ParkingTicketExpiredState(ParkingTicketState):
    def promote(self):
        print("Can not change state now !!")
