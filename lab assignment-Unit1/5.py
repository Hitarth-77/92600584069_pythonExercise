list = [10,21,32,40,43,54,65,76,87,98,100]
print('Original List : ',list)

# indexing
print("\n--- Indexing ---")
print("First element:", list[0])
print("Last element:", list[-1])
print("Element at index 3 :", list[3])

# slicing
print("\n--- Slicing ---")
print("First 3 elements         :", list[:3])
print("Elements from index 2 to 5:", list[2:6])
print("Every second element     :", list[::2])
print("Reversed list            :", list[::-1])

# Manipulation
print("\n--- Manipulation ---")
list.append(80)       
print("After append:", list)

list.insert(2, 25)    
print("After insert:", list)

list.remove(40)       
print("After remove:", list)

list.pop()            
print("After pop:", list)

# List Comprehensions
print("\n--- List Comprehensions ---")

squares = [x**2 for x in range(1, 6)]
print("Squares (1 to 5):", squares)

evens = [x for x in list if x % 2 == 0]
print("Even numbers from list:", evens)

uppercase = [ch.upper() for ch in ["a", "b", "c", "d"]]
print("Uppercase letters:", uppercase)

