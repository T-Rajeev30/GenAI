# 1. Introduction to Lists
# Lists are ordered, mutable collections that can hold items of any type.

# 2. Creating Lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 42, 3.14, True]

# 3. Accessing List Elements
print("First element:", numbers[0])      # 1
print("Last element:", numbers[-1])      # 5

# 4. Modifying List Elements
numbers[2] = 99
print("Modified numbers:", numbers)      # [1, 2, 99, 4, 5]

# 5. List Methods
numbers.append(6)                        # Add to end
numbers.insert(1, 100)                   # Insert at index 1
print("After append & insert:", numbers)

removed = numbers.pop()                  # Remove last element
print("Popped value:", removed)
numbers.remove(99)                       # Remove first occurrence of 99
print("After remove:", numbers)
print("Index of 100:", numbers.index(100))
numbers.reverse()
print("Reversed:", numbers)
numbers.sort()
print("Sorted:", numbers)

# 6. Slicing Lists
print("Slice [1:3]:", numbers[1:3])      # Elements at index 1 and 2
print("Slice [:2]:", numbers[:2])        # First two elements
print("Slice [2:]:", numbers[2:])        # From index 2 to end

# 7. Iterating Over Lists
print("Iterating:")
for item in mixed:
    print(item)

# 8. List Comprehensions
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# 9. Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Element at row 2, col 3:", matrix[1][2])  # 6

# 10. Practical Examples and Common Errors

# Example: Filtering even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# Common Error: IndexError
try:
    print(numbers[100])  # Out of range
except IndexError as e:
    print("IndexError:", e)

# Common Error: ValueError
try:
    numbers.remove(999)  # 999 not in list
except ValueError as e:
    print("ValueError:", e)