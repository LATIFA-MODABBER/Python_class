import re
import os

wrd = str(input("Enter the word: "))

print(re.search(r"^ab*$", wrd))

print(re.findall(r"ab{2,3}", wrd))

print(re.findall(r"[a-z]+(_[A-Z]+)*", wrd))

print(re.findall(r"[A-Z][a-z]+", wrd))

print(re.findall(r"a.*b$", wrd))

print(re.sub(r"[,\. ]", ":", wrd))

parts = wrd.split("_")
camel = parts[0]+"".join(word.capitalize() for word in parts[1:])
print(camel)

print(re.findall(r"[A-Z][a-z]*", wrd))

print((re.sub(r"([A-Z])", r" \1", wrd)).strip())

print((re.sub(r"([A-Z])", r"_\1", wrd)).lower())

