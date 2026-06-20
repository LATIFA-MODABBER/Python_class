# 1
students = [("xmili", 25), ("Bob", 32), ("zlice", 21)]
sorted_s = sorted(students, key=lambda x: x[1])
print(sorted_s)

# 2
price = []
while True:
    a = float(input("Enter prices: "))
    if a == 0:
        break
    price.append(a)
sorted_price = sorted(price)
print(sorted_price)

# 3
names = []
while True:
    name = str(input("Enter the names: "))
    if name == 'finished':
        break
    names.append(name)

new = sorted(names, key=lambda i : len(i))
print(new)

# 4 
dates = []

while True:
    dates = input("Enter the dates: ")
    if dates == 'finished !':
        break
    year, month, day = map(int, dates.split("."))
sorted_d = sorted(dates, reverse=True)

for y, m, d in sorted_d:
    print(f"{y}.{m}.{d}")

