# Task 1 a variable with different values
x = 4
x = "Salam"
print (x)

# Task 2 geting type of the variable
u = 90.0
print(type(u))

# Taks 3 assining multipule variable to one value or visversa
t = v = q = "Orange"
print(x, v, q)
tt, vv, qq = "orange", "Banana", "Cherry"
print(tt, vv, qq)

#Task 4 Global and Local varaiables
def myfunc():
    global a
    a = "python"
    print(a)
myfunc()

print("Programming language " + a)

# Task 5 to change the value of a global variable inside a function
b = "awesome"
def func():
    global b
    b = "fantastic"
func()

print("python is " + b)

