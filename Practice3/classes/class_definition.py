class mycls:
    x = 'Weclome'
    y = 'Dear'
    n = input("Enter name: ")

p1 = mycls()
p2 = mycls()
p3 = mycls()

print(p1.x, end=" ")
print(p2.y, end=" ")
print(p3.n)

class numbers:
    pass

a = numbers()
del a

class num:
    x = 2
    y = 3
    w = 4
    s = x+y+w
b = num()
print(b.s)

class day:
    s = 'sunday'
    s= 'satarday'
    m = 'monday'
c = day()
print(c.s)
