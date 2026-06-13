#Task 1: 
num = 1
while num < 10:
    num += 1
    if num == 3:
        continue
    print(num)

# Task 2: print only odd numbers
number = 0
while number is range(1, 11):
    number += 1
    if number % 2== 0:
        continue
    print(number)

# Task 3: 
while True:
    w = int(input())
    if w < 0:
        continue
    if w == 0:
        break
    print(w)