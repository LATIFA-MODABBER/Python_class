class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()

class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    pass

student = Student()
student.introduce()

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    pass

car = Car()
car.move()

class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    pass

circle = Circle()
circle.draw()