# Task 1: login Access
username = str(input())
if username == 'admin':
    print("Access granted! ")
else:
    print("Access denied! ")

# Task 2: validing a conditon
usernm = input()
if len(usernm) > 0:
    print(f'Wecome, {usernm}!')
else:
    print("Username cannot be empty! ")
# Task 3:  
a = 300
b = 5
if a % b == 0 :
    print("'a' is divisible by 'b'. ")
else :
    print("'a' is not a factor of 'b'. ")