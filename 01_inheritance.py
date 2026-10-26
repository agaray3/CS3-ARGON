class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is doing daily tasks."

    def annual_pay(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is leading a team of {self.team_size}."

    def approve_leave(self, employee: Employee):
        return f"{self.name} approved leave for {employee.name}."


if __name__ == "__main__":
    staff = Employee("Maria", 25000)
    boss = Manager("Carlos", 60000, team_size=5)

    print(staff.work())                
    print(boss.work())     
    print(f"Inherited annual_pay(): {boss.annual_pay()}")
    print(boss.approve_leave(staff)) 
    print(f"Is Manager an Employee? {isinstance(boss, Employee)}")
