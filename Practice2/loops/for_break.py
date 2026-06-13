# Task 1:
students = ["Ali", "Sara", "John", "Emma", "David"]

for student in students:
    if student == "Emma":
        print("Student found!")
        break

    print("Checking", student)

# task 2:
numbers = [13, 25, 34, 42, 56, 70]

for num in numbers:
    if num % 7 == 0:
        print("First number divisible by 7:", num)
        break

# Task 3:
scores = [85, 92, 78, 61, 45, 88]

for score in scores:
    if score < 50:
        print("A student has failed with score:", score)
        break

    print("Passed score:", score)
    
