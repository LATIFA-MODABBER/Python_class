class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

cat = Cat()
cat.speak()

class Person:
    def job(self):
        print("Works")

class Teacher(Person):
    def job(self):
        print("Teaches students")

teacher = Teacher()
teacher.job()

class Vehicle:
    def move(self):
        print("Moving")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

bike = Bicycle()
bike.move()

class Shape:
    def area(self):
        print("Unknown area")

class Square(Shape):
    def area(self):
        print(5 * 5)

square = Square()
square.area()

