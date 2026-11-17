class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.__age
    
person1 = Person("Lina", 20)
print("Name:",person1.name) 
print("Age:",person1.get_age())   

# Reflection: Accessing __age through get_age() protects the data from accidental direct modification and allows us to control how the value is viewed or validated.
