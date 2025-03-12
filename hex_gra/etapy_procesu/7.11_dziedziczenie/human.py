import random

none = 0
naucz = 1
mc = 2

class Human:
    def __init__(self, name, age, employ):
        self.name = name
        self.age = age
        self.employ = employ
        if employ == none:
            self.benefit = 0.5
        else:
            self.benefit = 0
        
    def happyness(self):
        return (100-self.age)*(self.employ + self.benefit)

class Student(Human):
    def __init__(self, name, age, oceny, pocket):
        super().__init__(name, age, none)
        self.oceny = oceny
        self.pocket = pocket

    def happyness(self):
        return self.age*(self.oceny + self.pocket/1000)


pan_grzegorz = Human("grzes", 42, none)
pan_adam = Student("adas", 27, 3.2, 1200)


print(pan_grzegorz.happyness())
print(pan_adam.happyness())
