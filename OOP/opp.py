import datetime

class Employee:
    
    classVariable = 1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
    
    def details(self):
        return 'Name: ' + self.name + ' Salary: ' + str(self.salary)
    
    @classmethod
    def setClassVariable(cls, classVariable):
        #pass
        cls.classVariable = classVariable
    
    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_1 = Employee('Raul', 43000)
emp_2 = Employee('Test', 77600)

myDate = datetime.date(2020, 5, 15)

print(emp_1.isWorkday(myDate))