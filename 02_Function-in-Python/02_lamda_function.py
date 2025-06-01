# 02_lambda_function.py

# A lambda function is a small anonymous function.
# It can take any number of arguments, but can only have one expression.

# Syntax:
# lambda arguments: expression

# Example 1: Add two numbers
add = lambda x, y: x + y
print("Sum:", add(2, 3))  # Output: 5

# Example 2: Square a number
square = lambda x: x ** 2
print("Square:", square(4))  # Output: 16

# Example 3: Use with sorted()
points = [(2, 3), (1, 2), (4, 1)]
points_sorted = sorted(points, key=lambda point: point[1])
print("Sorted by second value:", points_sorted)

# Example 4: Use with map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print("Squared list:", squared)

# Example 5: Use with filter()
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)