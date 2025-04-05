from app.observers import Observer
from app.payment import Payment, CashPayment
from app.vehicle import Vehicle
from app.strategy import FirstSpotStrategy
from app.ticket import ParkingTicket


class EntryGate:
    def __init__(self, name):
        self.name = name

    def generate_ticket(self, spot) -> ParkingTicket:
        ticket = ParkingTicket(self, spot)
        return ticket

    def __repr__(self):
        return self.name


class ExitGate:
    def __init__(self, name):
        self.name = name

    def process_ticket(self, vehicle: Vehicle, payment_mode: Payment):
        ticket = vehicle.get_ticket()

        amount = ticket.calculate_charge()
        payment_status = self.make_payment(amount, payment_mode)

        ticket.promote()

        if payment_status:
            ticket.close(self.name)

    @staticmethod
    def make_payment(amount, payment_mode: Payment):
        status = payment_mode.process(amount)
        return status

    def __repr__(self):
        return self.name


class ParkingLot:
    def __init__(self, floors, entry_gates, exit_gates):
        self.floors = floors
        self.entry_gates = entry_gates
        self.exit_gates = exit_gates
        self.vehicles = []
        self.listeners = []

    def park(self, vehicle, entry_gate, parking_strategy=FirstSpotStrategy()):
        spot = parking_strategy.park(vehicle, self.floors)
        if not spot:
            message = "No Spots left"
            print(message)
            self.notify(message)
            return None

        ticket = entry_gate.generate_ticket(spot)
        ticket.promote()
        vehicle.assign_ticket(ticket)

        spot.occupy(vehicle)
        self.update_subs()

        return ticket

    def free(self, vehicle: Vehicle, exit_gate: ExitGate, payment_mode: Payment):
        exit_gate.process_ticket(vehicle, payment_mode)
        self.update_subs()

    def subscribe(self, observer: Observer):
        self.listeners.append(observer)

    def update_subs(self):
        for listener in self.listeners:
            for floor in self.floors:
                if floor == listener.get_floor():
                    listener.update(floor.get_spots())

    def notify(self, message):
        for listener in self.listeners:
            listener.show_message(message)

    def get_all_free_spots(self):
        free_spots = []
        for floor in self.floors:
            print(floor, end=" - ")
            for spot in floor.get_spots():
                if spot.is_free():
                    free_spots.append((floor, spot))
                    print(spot, end=" ")
            print()

        return free_spots

    @staticmethod
    def release_spot(spot):
        spot.free()
