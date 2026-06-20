# 1
numbers = []
while True:
    a = int(input("Enter numbers: "))
    if a == 0:
        break
    numbers.append(a)
even_numbers = list(filter(lambda i : i %2 == 0, numbers))
print(even_numbers)

# 2
scores = []
while True:
    a = int(input("Enter scores: "))
    if a == 0:
        break
    scores.append(a)
high_scores = list(filter(lambda i: i >= 85, scores))
print(high_scores)

# 3
strings = []

while True:
    a = str(input("Enter words: "))
    if a.lower() == 'stop':
        break
    strings.append(a)
specific = list(filter(lambda i : len(i)>= 5, strings))
print(specific)

# 4 if a number is a multiple of 3
num = []
while True:
    a = int(input("Enter numbers: "))
    if a == 0:
        break
    num.append(a)

filtered = list(filter(lambda i: i%3== 0, num))
print(filtered)
