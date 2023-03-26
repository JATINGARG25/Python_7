
#  This is a Single inheritance

class Employee:
    company = "Google"

    def showdetails(self):
        print("This is an employee.")

class Programmer(Employee):
                                      # company = "Youtube"
    language = "Python"
    def getname(self):
        print(f"The language is {self.language}")

                                      # def showdetails(self):
                                      #     print("This is a Programmer.")

e = Employee()
e.showdetails()
p = Programmer()
p.showdetails()
print(p.company)
