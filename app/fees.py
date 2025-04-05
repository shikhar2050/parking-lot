from abc import ABC, abstractmethod


class FeeVisitor(ABC):

    @abstractmethod
    def visit_compact(self, compact_spot):
        pass

    @abstractmethod
    def visit_large(self, large_spot):
        pass

    @abstractmethod
    def visit_xl(self, xl_spot):
        pass


class Fee(FeeVisitor):

    def visit_compact(self, compact_spot):
        return compact_spot.get_charge() * 1.05 * Fee.dynamic_pricing()

    def visit_large(self, large_spot):
        pass

    def visit_xl(self, xl_spot):
        pass

    @staticmethod
    def dynamic_pricing():
        return 1



