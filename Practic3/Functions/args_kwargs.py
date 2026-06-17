def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function('Emili', 'Toba', 'Lila')

def kids_name(*args):
    print("Type: ", type(args))
    print("First argument: ", args[0])
    print("Second argument: ", args[1])
    print("Third arguments: ", args[2])
    print("all of them: ", args)

kids_name('Lila', 'Ema', 'Sundy', 'Jordan', 'Jseka')   # ,*name--- args; *, name --- keyword arguments

def greating(great, *names):
    for i in names:
        print(great + i)

greating("Hello, ", 'Alic', 'Sara', 'Bob', 'Mom', 'Dad')

def sum(*num):
    total = 0
    for i in num:
        total += i
    return total

numbers = []
while True:
    n = int(input("Enter nums: "))
    if n == 0:
        break
    numbers.append(n)
result = sum(*numbers)
print("Total is: ", result)

# finding the max in the numbers

def mx(*nums):
    if len(nums)== 0:
        return None
    max_num = nums[0]
    for i in nums:
        if i > max_num:
            max_num = i 
    return max_num

num_x = []

while True:
    try:
        n = int(input("Enter numbers: "))
        num_x.append(n)
    except ValueError:
        break

result = mx(*num_x)
print("Mx num is: ", result)