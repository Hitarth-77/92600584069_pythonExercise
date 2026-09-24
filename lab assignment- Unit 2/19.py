# Iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:", numbers)

# Convert iterable into iterator
it = iter(numbers)

print("Iterator values:")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))