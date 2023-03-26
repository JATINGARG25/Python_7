class Animals:
    type = "mammal"

class Pets(Animals):
    type = "white"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()
