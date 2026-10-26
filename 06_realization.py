"""Realization / Implementation (Implements): classes fulfil a Notifier interface.

Python has no 'interface' keyword, so the abc module is used. Every
concrete class MUST implement the abstract method(s), and the interface
itself cannot be instantiated.
"""

from abc import ABC, abstractmethod


class Notifier(ABC):  # The "interface"
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass


class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"[EMAIL to {recipient}] {message}")


class SMSNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS to {recipient}] {message}")


# An incomplete class: it forgets to implement send()
class BrokenNotifier(Notifier):
    pass


if __name__ == "__main__":
    # Both realizations can be used through the same interface type
    channels = [
        (EmailNotifier(), "juan@example.com"),
        (SMSNotifier(), "+63 917 123 4567"),
    ]
    for channel, recipient in channels:
        channel.send(recipient, "Your order has shipped!")

    # Interface and incomplete implementations cannot be instantiated
    for cls in (Notifier, BrokenNotifier):
        try:
            cls()
        except TypeError as e:
            print(f"\n{cls.__name__} -> TypeError: {e}")
