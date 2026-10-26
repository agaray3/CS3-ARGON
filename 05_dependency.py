class CoffeeMachine:
    def brew(self, drink: str) -> str:
        return f"{drink} brewed"


class Barista:
    def __init__(self, name: str):
        self.name = name

    def serve(self, drink: str, machine: CoffeeMachine):
        result = machine.brew(drink)
        print(f"{self.name} served: {result}")


if __name__ == "__main__":
    shop_machine = CoffeeMachine()
    
    barista = Barista("Liza")

    barista.serve("Caffe Latte", shop_machine)
    
    print(f"Barista keeps a machine reference? {hasattr(barista, 'machine')}")
