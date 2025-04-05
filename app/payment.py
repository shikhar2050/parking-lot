from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process(self, amount):
        pass


class UPIPayment(Payment):

    def process(self, amount):
        print("Process UPI payment")
        return True


class CardPayment(Payment):

    def process(self, amount):
        print("Process Card payment")
        return True


class CashPayment(Payment):

    def process(self, amount):
        print("Process Cash payment")
        return True

