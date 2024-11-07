class Human:
    def __init__(self,name,age,employment,money):
        self.name = name
        self.age = age
        self.employment = employment
        self.money = money
        if employment == 0:
            money == 0.5
    def happyness(age,employment,money):
        return (100-age/2)*(employment*money)

class Student:
    def __init__(self,name,age,gradesavg,money,hobby):
        super().__init__(name,age,money,0)
        self.gradesavg=gradesavg
        self.hobby=hobby
    def happyness(age,hobby,money):
        return (100-age/2)*(hobby*money)
    
noipanapawel = Student("pablo" , 20 , 2.0 , 1000 ,1000)
Gregor = Human("Grzeg", 100 , 1 , 10)
