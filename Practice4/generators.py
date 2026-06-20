# 1
def my_generator():
    yield 1
    yield 2
    yield 3

for i in my_generator():
    print(i, end=" ")
print('\n')
#2
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for i in count_up_to(6):
    print(i, end=" ")
print('\n')

# 3
def large_seq(n):
    for i in range(n):
        yield i
# for i in large_seq(12):
#     print(i, end=" ")

gen = large_seq(12)
print(next(gen))
print(next(gen))
print(next(gen))

# 4
myTuple = ('apple', 'banana','chreey')
myIt = iter(myTuple)

for i in myTuple:
    print(i)

print(next(myIt))
print(next(myIt))
print(next(myIt))

# 5
myStr = 'banana'
myit = iter(myStr)
for i in myStr:
    print(i)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# 6
class myNum:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x

myc = myNum()
myit = iter(myNum)

print(next(myit))
print(next(myit))
print(next(myit))

# 7
class myn:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myx = myn()
y = iter(myn)
for x in y:
    print(x)
    