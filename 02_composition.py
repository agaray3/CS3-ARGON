"""Composition (Strong Has-a): the parent owns the lifetime of its child objects."""


class Room:
    def __init__(self, name: str):
        self.name = name

    def __del__(self):
        print(f"Room destroyed: {self.name}")


class House:
    def __init__(self):
        # The House creates and owns these Room objects directly
        self.rooms = [Room("Kitchen"), Room("Bedroom")]

    def __del__(self):
        print("House destroyed.")


if __name__ == "__main__":
    # 1. Instantiate the parent object (House)
    my_house = House()

    # 2. Iterate through the child objects created inside it
    for room in my_house.rooms:
        print(f"Room created: {room.name}")

    # 3. Deleting the House also destroys the Rooms it owns
    print("\nExecuting: del my_house")
    del my_house
