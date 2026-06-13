# Task 1:
students = ["Ali", "Sara", "Absent", "John", "Absent", "Emma"]

for student in students:
    if student == "Absent":
        continue

    print(student, "is present")

# Task 2:
numbers = [12, -5, 8, -2, 15, -7, 20]

for num in numbers:
    if num < 0:
        continue

    print(num)

# Task 3:
scores = [85, 42, 91, 38, 76, 49, 88]

for score in scores:
    if score < 50:
        continue

    print("Passing score:", score)