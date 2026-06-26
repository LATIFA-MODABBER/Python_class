from functools import reduce

# ---------- map() example ----------
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("\nSquared numbers using map():", squared)


# ---------- filter() example ----------
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)


# ---------- reduce() example ----------
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce():", sum_all)
