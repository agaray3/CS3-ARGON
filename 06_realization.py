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


class BrokenNotifier(Notifier):
    pass


if __name__ == "__main__":
    channels = [
        (EmailNotifier(), "juan@example.com"),
        (SMSNotifier(), "+63 917 123 4567"),
    ]
    for channel, recipient in channels:
        channel.send(recipient, "Your order has shipped!")

    for cls in (Notifier, BrokenNotifier):
        try:
            cls()
        except TypeError as e:
            print(f"\n{cls.__name__} -> TypeError: {e}")
