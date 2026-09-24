def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Taking input from user
n = int(input("Enter the number: "))

print("Generated sequence:")

for number in generate_numbers(n):
    print(number)