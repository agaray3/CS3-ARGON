"""Inheritance (Is-a): the child class inherits directly from the parent class."""


class Animal:
    def __init__(self, name: str):
        self.name = name


# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


if __name__ == "__main__":
    # 1. Instantiate a Dog with a name passed up to the Animal parent
    my_dog = Dog("Buddy")

    # 2. Use the inherited attribute and the unique subclass method
    print(f"Inherited attribute -> name: {my_dog.name}")
    print(my_dog.bark())
