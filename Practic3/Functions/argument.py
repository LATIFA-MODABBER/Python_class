# 1
def full_name(fname):
    print(fname + 'Modabber')

full_name('Waez ')
full_name('Latifa ')
full_name('Hashim ')
full_name('Yasin ')

# 2
def log_in(username, password):
    if username == 'l_modabber@kbtu.kz' and password == 'canada.live.20.27':
        return 'Welcome! '
    
username = str(input("Enter your usernmae: "))
password = str(input("Enter your password: "))
result = log_in(username, password)
print(result)

#3
def user(name = 'customer'):
    print('Hello dear, ', name)

user('Alice ')
user()

# 4 in case of several arguments using '=' the order of the argument does not matter

def animal(clas, name):
   print("This animal is from ", clas, " Group.")
   print("I have a ", name, " which belongs to ", clas)

animal( name = 'Cat',clas = 'Memmal ')  # keyword argument
animal('Birds', 'duck')  # positional argument

def pets(animal, name, age):
    print("I have a ", age, "year old ", animal, ". It's name is ", name)

pets('Cat', age = 4, name = 'Buddy')  # mixed arguments

# 5 different data types are arguments: lists, tuples, dictionaries, sets

def my_function(fruits):  # list
    x = 1
    for i in fruits:
        print(x, ", ", i)
        x += 1
    print('\n')

my_fruits = ['apple', 'banana', 'cherry']
my_function(my_fruits)

# 6 dictionary argument
def my_function(person):
    print("Name: ", person["name"])
    print("Age: ", person["age"])
per = {"name" : "Emili", "age": 25}
my_function(per)

