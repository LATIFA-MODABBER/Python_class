# Task 1: Temorature
temp = 20
if temp > 30:
    print("It's hot outside!")
elif temp > 20:
    print("It's warm outside! ")
elif temp > 10:
    print("It's cool outside!")
else:
    print("It's cold outside!")

#Task 2: Grading

score = input()

if score >89 :
    print("Grade A")
elif score > 79:
    print("Grade B")
elif score > 59:
    print("Grade D")
else:
    print("Fail")

# Task 3: age catagory
age = 90
if age < 13:
    print("You are a child!")
elif age >= 13 and age < 20:
    print("You are a teenager!")
elif age >= 20 and age < 65:
    print("You are an adult!")
else:
    print("You are a snior!")