from functools import reduce


# ---------- enumerate() example ----------
fruits = ["apple", "banana", "mango"]
print("\nEnumerate example:")
for index, fruit in enumerate(fruits):
    print(index, fruit)


# ---------- zip() example ----------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

print("\nZip example:")
for name, score in zip(names, scores):
    print(name, score)


# ---------- Type checking and conversions ----------
value = "123"

print("\nType checking:")
print(type(value))

# conversion
value_int = int(value)
value_float = float(value_int)

print("Converted to int:", value_int)
print("Converted to float:", value_float)
print("Type after conversion:", type(value_float))