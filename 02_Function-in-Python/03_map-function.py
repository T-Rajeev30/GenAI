# 03_map-function.py

"""
This script explains the `map` function in Python with descriptive comments and examples.

The `map` function applies a given function to all items in an input iterable (like a list) and returns a map object (which is an iterator).
You can convert the result to a list, tuple, etc., if you want to see the results directly.

Syntax:
    map(function, iterable, ...)

- function: A function that will be applied to each item.
- iterable: One or more iterables whose items will be passed to the function.

Let's see some examples:
"""

# Example 1: Using map to square each number in a list

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)  # Returns a map object

print("Squared numbers:", list(squared_numbers))  # Convert to list to display results

# Example 2: Using map with lambda function to double each number

doubled_numbers = map(lambda x: x * 2, numbers)
print("Doubled numbers:", list(doubled_numbers))

# Example 3: Using map with multiple iterables

a = [1, 2, 3]
b = [4, 5, 6]
summed = map(lambda x, y: x + y, a, b)
print("Sum of elements from two lists:", list(summed))

# Example 4: Converting all strings in a list to uppercase

words = ['python', 'map', 'function']
uppercased = map(str.upper, words)
print("Uppercased words:", list(uppercased))

"""
Key Points:
- `map` is useful for applying a function to each item in an iterable.
- The result is a map object (an iterator), so you often need to convert it to a list or tuple.
- You can use built-in functions, user-defined functions, or lambda expressions with map.
- If multiple iterables are passed, the function must take as many arguments as there are iterables, and mapping stops at the shortest iterable.
"""