# Task 1:
while True:
    num = input()
    if num < 0:
        break
    print(num)

# Task 2:

secret = 7

while True:
    guess = int(input())

    if guess == 7:
        print("Correct!")
        break
    print("Try again! ")

# Task 3: print numbers until a multiple of 7 is found
while True:
    password = input('Enter your password! ')
    if password == 'ijk123':
        print('Welcome! ')
        break
    print('Incorrect entery! ')

