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
        self.engine = Engine(horsepower)

    def drive(self):
        return f"{self.model}: {self.engine.start()} Driving!"

    def __del__(self):
        print(f"Car '{self.model}' destroyed.")


if __name__ == "__main__":
    my_car = Car("Toyota Vios", 106)
    print(my_car.drive())

    print("\nExecuting: del my_car")
    del my_car
