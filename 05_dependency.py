"""Dependency (Uses-a): a Barista USES a CoffeeMachine temporarily.

The machine is only a method parameter. It is never stored as an
attribute, so the link ends the moment the method returns.
"""


class CoffeeMachine:
    def brew(self, drink: str) -> str:
        return f"{drink} brewed"


class Barista:
    def __init__(self, name: str):
        self.name = name  # note: no CoffeeMachine attribute here

    # Depends on CoffeeMachine only for the duration of this call
    def serve(self, drink: str, machine: CoffeeMachine):
        result = machine.brew(drink)
        print(f"{self.name} served: {result}")


if __name__ == "__main__":
    shop_machine = CoffeeMachine()
    barista = Barista("Liza")

    # The machine is handed over just for this one call
    barista.serve("Caffe Latte", shop_machine)

    # Proof that the reference was never stored permanently
    print(f"Barista keeps a machine reference? {hasattr(barista, 'machine')}")
