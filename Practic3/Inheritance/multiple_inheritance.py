class Fly:
    def fly(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

duck = Duck()
duck.fly()
duck.swim()

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skill1()
child.skill2()

class Writer:
    def write(self):
        print("Writing")

class Speaker:
    def speak(self):
        print("Speaking")

class Author(Writer, Speaker):
    pass

author = Author()
author.write()
author.speak()

class Camera:
    def photo(self):
        print("Taking photo")

class Phone:
    def call(self):
        print("Calling")

class Smartphone(Camera, Phone):
    pass

mobile = Smartphone()
mobile.photo()
mobile.call()