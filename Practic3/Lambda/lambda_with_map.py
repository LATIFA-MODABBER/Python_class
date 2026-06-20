# 1
numbers = []
while True:
    a = int(input("Enter numbers: "))
    if a == 0:
        break
    numbers.append(a)

dauble = list(map(lambda i : i *2, numbers))
#2
names = []
while True:
    name = str(input("Enter names: "))
    if name == 'finished':
        break
    names.append(name)
up_name = list(map(lambda i : i.upper(), names))
print(up_name)

# 3
students = []
while True:
    try:
        gpa = float(input("Enter precentage: "))
    except ValueError:
        print("Only numbers are allowed!")
        break
    students.append(gpa)

gpa_a = list(map(lambda x: x*4/100, students))
print(gpa_a)

# 4 find length of strings
strings = []
while True:
    word = input("Enter your word")
    if word.lower == 'stop':
        break
    strings.append(word)
lengths = list(map(lambda s: len(s), strings))
print(lengths)

