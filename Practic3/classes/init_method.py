class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("Emil", 36)
print(p1.name)
print(p1.age)

# 2
class prsn:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter name: ")
age = int(input("Enter age: "))

p2 = prsn(name, age)
print(p2.name)
print(p2.age)

class prsn:
    pass
p1 = prsn()
p1.name = input("enter name: ")
p1.age = int(input("enter age: "))
print(p1.name)
print(p1.age)

class student:
    def __init__(self, name, group = "Second"):
        self.name = name
        self.group = group

name = input("Enter student name: ")
a = student(name)
print(a.name,"is in", a.group, "group.")



class student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

frist_hour = [
    student("Alice", "First"),
    student("Bob", "First"),
    student("Charlie", "First")
]

second_hour = [
    student("David", "Second"),
    student("Eve", "Second"),
    student("Frank", "Second")
]



for student in frist_hour:
    print(f"  _{student.name}")

for student in second_hour:
    print(f"  _{student.name}")

all_students = frist_hour + second_hour

for student in all_students:
    print(f"{student.name} is in {student.group} group.")

class person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

pa = person('Alic', 25, 'New Yourk', 'USA')
print(pa.name)
print(pa.age)
print(pa.city)
print(pa.country)