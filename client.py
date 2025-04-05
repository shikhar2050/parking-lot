from app.observers import ParkingDisplayBoard
from app.parking_lot import ParkingLot, EntryGate, ExitGate
from app.payment import CashPayment
from app.spot import CompactSpot, LargeSpot, XLSpot, ParkingFloor
from app.vehicle import VehicleFactory

spot1 = CompactSpot('spot1')
spot2 = LargeSpot('spot2')
spot3 = XLSpot('spot3')

floor0 = ParkingFloor('floor0')
floor0.add_spot(spot1)
# floor0.add_spot(spot2)
# floor0.add_spot(spot3)

spot4 = CompactSpot('spot4')
spot5 = LargeSpot('spot5')
spot6 = LargeSpot('spot6')
spot7 = XLSpot('spot7')

floor1 = ParkingFloor('floor1')
# floor1.add_spot(spot4)
# floor1.add_spot(spot5)
# floor1.add_spot(spot6)
floor1.add_spot(spot7)

entry_gate1 = EntryGate("Entry1")
entry_gate2 = EntryGate("Entry2")

exit_gate1 = ExitGate("Exit1")
exit_gate2 = ExitGate("Exit2")
exit_gate3 = ExitGate("Exit3")

board0 = ParkingDisplayBoard(floor0)
board1 = ParkingDisplayBoard(floor1)

parking_lot = ParkingLot([floor0, floor1], [entry_gate1, entry_gate2], [exit_gate1, exit_gate2, exit_gate3])
parking_lot.subscribe(board0)
parking_lot.subscribe(board1)

V1 = VehicleFactory().get_vehicle('Bike')
V2 = VehicleFactory().get_vehicle('Bike')
V3 = VehicleFactory().get_vehicle('Car')
V4 = VehicleFactory().get_vehicle('Truck')

print("=============================")
print("=============================")
parking_lot.get_all_free_spots()

print("=============================")
tkt = parking_lot.park(V1, entry_gate1)
tkt.print_ticket()
parking_lot.get_all_free_spots()

print("=============================")
tkt2 = parking_lot.park(V4, entry_gate2)
tkt2.print_ticket()
parking_lot.get_all_free_spots()

print("=============================")
parking_lot.free(V1, exit_gate3, CashPayment())
parking_lot.get_all_free_spots()
tkt.print_ticket()
tkt2.print_ticket()


