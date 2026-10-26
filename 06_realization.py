"""Realization / Implementation (Implements): a class fulfils an interface (abc module)."""

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):  # The "interface"
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


# GCashPayment realizes/implements PaymentProcessor
class GCashPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PHP {amount} via GCash.")
        return True


if __name__ == "__main__":
    # 1. Instantiate the concrete implementation class
    gateway = GCashPayment()

    # 2. Invoke the realized method
    success = gateway.process_payment(250.75)
    print(f"Payment Status: {success}")

    # The interface itself cannot be instantiated
    try:
        PaymentProcessor()
    except TypeError as e:
        print(f"\nAs expected, the interface can't be instantiated: {e}")
