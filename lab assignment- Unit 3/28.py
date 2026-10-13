import re

text = "My name is Hitarth and my age is 22."

if re.search(r"\d+", text):
    print("Number found")

numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

words = re.findall(r"\w+", text)
print("Words:", words)