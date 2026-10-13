import re

text = "Python is easy. Python is powerful."

m = re.match(r"Python", text)
s = re.search(r"easy", text)
f = re.findall(r"Python", text)

print("Match:", m.group() if m else "Not found")
print("Search:", s.group() if s else "Not found")
print("Findall:", f)