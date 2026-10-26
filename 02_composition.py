"""Composition (Strong Has-a): a Car OWNS its Engine.

The Engine is created INSIDE the Car's constructor, so it cannot exist
without the Car. When the Car is destroyed, so is the Engine.
"""


class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self):
        return f"Engine ({self.horsepower} hp) started."

    def __del__(self):
        print(f"Engine ({self.horsepower} hp) destroyed.")


class Car:
    def __init__(self, model: str, horsepower: int):
        self.model = model
        # The Car creates and owns its Engine; nobody outside supplies it
        self.engine = Engine(horsepower)

    def drive(self):
        return f"{self.model}: {self.engine.start()} Driving!"

    def __del__(self):
        print(f"Car '{self.model}' destroyed.")


if __name__ == "__main__":
    my_car = Car("Toyota Vios", 106)
    print(my_car.drive())

    # Deleting the whole (Car) also destroys the part (Engine)
    print("\nExecuting: del my_car")
    del my_car
