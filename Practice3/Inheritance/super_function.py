class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Tom", 10)
print(s.name, s.grade)

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")

dog = Dog()
dog.speak()

class Employee:
    def __init__(self, company):
        self.company = company

class Manager(Employee):
    def __init__(self, company, department):
        super().__init__(company)
        self.department = department

m = Manager("Google", "IT")
print(m.company)
print(m.department)


class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car ready")

car = Car()
car.start()
