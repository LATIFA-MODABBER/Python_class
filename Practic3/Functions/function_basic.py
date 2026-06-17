def my_function():
    print('Hello from inside function!')

my_function()

def temp(fernehaid):
    print((fernehaid - 32)*5/9)

temp(45)

def empty():
    pass

def precentage_gpa(marks):
    return marks*4/100
marks = float(input("Enter your precentage: "))
gpa = precentage_gpa(marks)

print('GPA: ', gpa)


def gpa_precentage(marks):
    return marks*100/4

marks = float(input("Enter your GPA: "))
precentage = gpa_precentage(marks)

print('precentage: ', precentage)
