class Employee:
    company = "Bharat Gas"
    salary = 4500
    salarybonus = 500
    # totalsalary = 5000

    @property
    def totalsalary(self):
        return self.salary+self.salarybonus

    @totalsalary.setter
    def totalsalary(self,value):
        self.salarybonus = value - self.salary

e = Employee()
print(e.totalsalary)
e.totalsalary = 5800
print(e.salarybonus)
print(e.totalsalary)
