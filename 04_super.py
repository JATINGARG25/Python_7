class Person:
    country = "India"
    def takebreadth(self):
        print("I am breathing.")

class Employee(Person):
    company = "Honda"
    def salary(self):
        print(f"Salary is {self.salary}")
    def takebreadth(self):
        # *************use of super***************
 
        super().takebreadth()
        print("I am an employee so i am luckily breathing..")

class Programmer (Employee):
    company = "Fiverr"

    def salary(self):
        print(f"No salary to programmer")

p = Person()
e = Employee()
pr = Programmer()

p.takebreadth()
e.takebreadth()
pr.takebreadth()

