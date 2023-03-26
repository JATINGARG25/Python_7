class Employee:
    company = "Camel"
    salary = 1000
    location = "Jaipur"

    @classmethod
    def changesalary(cls,sal):
        cls.salary = sal

e = Employee()
print(e.salary)
print(Employee.salary)
e.changesalary(8745837)
print(e.salary)
print(Employee.salary)
