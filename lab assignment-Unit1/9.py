def add(a,b):
    print("Sum =", a+b)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
add(a,b)

def greet(name="Student"):
    print("Hello",name)
name = input("Enter your name:")
if name == "":
    greet()
else:
    greet(name)
def student(name,age):
    print("Name:",name)
    print("Age:",age)
name = input("Enter your name:")
age = int(input("Enter your age:"))
student(age=age,name=name)
