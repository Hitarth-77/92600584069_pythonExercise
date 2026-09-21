#List Comprehensive
numbers = [1,2,3,4,5]
square = [num*num for num in numbers]
print("List Comprehensive")
print(square)

#dictionary Comprehensive
numbers = [5,6,7,8,9]
square_dict = {num: num*num for num in numbers}
print("\nDictionary Comprehensive")
print(square)
#Set Comprehension
numbers = [1, 2, 2, 3, 3, 4, 5, 5]

square_set = {num * num for num in numbers}

print("\nSet Comprehension:")
print(square_set)
