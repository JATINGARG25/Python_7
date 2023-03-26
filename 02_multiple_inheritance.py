
#  in multi-level inheritance , there are more than one parent 

class Employee:
    company = "Google"
    ecode = 120

class Freelancer():
    company = "fiver"
    level = 0
    def upgrade(self):
        self.level = self.level+1

class Programmer(Employee,Freelancer):
    name = "rohit"

p = Programmer()
p.upgrade()
print(p.ecode)
print(p.level)
print(p.company)

