#JSON : JavaScript Object Notation
import json

x = '{"name":"John", "age":30, "city": "New York"}'
y = json.loads(x)

print(y["age"])

v = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
u = json.dumps(v)
print(u)

import json

print(json.dumps({"name": "john", "age": 34, "country": "usa"}))

b = {
    "name": "John",
    "age": 30, 
    "married": True,
    "divorced": False,
    "children": ("ana", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(b, indent=4, separators=(".", "=", sort_keys=True)))  # to json 
# print(json.loads(b)).   to python

