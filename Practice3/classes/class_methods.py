class person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello, my name is " + self.name)
    
pr = person("Emil")
pr.greet()


class cal:
    def add(self, a, b):
        return a+b
    def mult(self, a, b):
        return a*b
    
c = cal()
print(c.add(4, 2))
print(c.mult(4, 2))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()