import random

print("Random integer:", random.randint(1, 100))
print("Random float:", random.random())

fruits = ["Apple", "Mango", "Banana"]
print("Random fruit:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled list:", fruits)