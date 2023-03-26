class Employee:
    salary = 5000
    increment = 500

    @property
    def salaryafterincrement(self):
        return self.salary+self.increment

    @salaryafterincrement.setter
    def salaryafterincrement(self,value):
        self.increment = value - self.salary

a = Employee()
print(a.salaryafterincrement)

a.salaryafterincrement = 5800
print(a.increment)
