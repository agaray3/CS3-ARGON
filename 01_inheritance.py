"""Inheritance (Is-a): Manager IS-A Employee.

The child class inherits attributes and methods from the parent class,
and can extend or override them.
"""


class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is doing daily tasks."

    def annual_pay(self):
        return self.salary * 12


# Manager inherits everything from Employee
class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)  # reuse the parent's constructor
        self.team_size = team_size

    # Overrides the parent's method
    def work(self):
        return f"{self.name} is leading a team of {self.team_size}."

    # Unique to the subclass
    def approve_leave(self, employee: Employee):
        return f"{self.name} approved leave for {employee.name}."


if __name__ == "__main__":
    staff = Employee("Maria", 25000)
    boss = Manager("Carlos", 60000, team_size=5)

    print(staff.work())                        # parent behavior
    print(boss.work())                         # overridden behavior
    print(f"Inherited annual_pay(): {boss.annual_pay()}")  # inherited as-is
    print(boss.approve_leave(staff))           # subclass-only method
    print(f"Is Manager an Employee? {isinstance(boss, Employee)}")
