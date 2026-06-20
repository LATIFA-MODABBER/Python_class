# 1
x = lambda x, y: x+y
print(x(4,3))
# 2
x = lambda x, y, z, d: (x+y)/(z+d)
print(x(2, 3, 4 ,2))

# 3
def myfunc():
    n = float(input("Enter the cost: "))
    return lambda a = 0.02: a *n + n

total = myfunc()()
print("The total cost is $", total)

# 4

def multiply(n):
    return lambda a: pow(n, a)
print(multiply(2)(3))

# 5 area
import math
def area():
    radius = float(input("Enter radius: "))
    return lambda radius: math.pi *radius**2
print(area()())