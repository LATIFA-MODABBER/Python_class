import re

text1 = "abbb"
print(bool(re.fullmatch(r"ab*", text1)))

text2 = "abb"
print(bool(re.fullmatch(r"ab{2,3}", text2)))

text3 = "hello_world my_name is Python"
print(re.findall(r"\b[a-z]+_[a-z]+\b", text3))

text4 = "Hello World Python REGEX"
print(re.findall(r"\b[A-Z][a-z]+\b", text4))

text5 = "a123xyzb"
print(bool(re.fullmatch(r"a.*b", text5)))

text6 = "Hello, world. Python is fun"
print(re.sub(r"[ ,.]", ":", text6))

text7 = "my_first_program"
camel = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text7)
print(camel)

text8 = "MyFirstProgram"
parts = [x for x in re.split(r"(?=[A-Z])", text8) if x]
print(parts)

text9 = "MyFirstProgram"
spaced = re.sub(r"([A-Z])", r" \1", text9).strip()
print(spaced)

text10 = "myFirstProgram"
snake = re.sub(r"([A-Z])", r"_\1", text10).lower()
print(snake)