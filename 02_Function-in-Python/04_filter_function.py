# 04_filter_function.py

"""
This script explains the `filter()` function in Python with descriptive comments and examples.

The `filter()` function is used to filter elements from an iterable (like a list, tuple, etc.)
based on a function that returns either True or False for each element.

Syntax:
    filter(function, iterable)

- function: A function that tests each element of the iterable. It should return True or False.
- iterable: The sequence to be filtered.

The result is an iterator containing only the elements for which the function returns True.
"""

# Example 1: Filtering even numbers from a list

def is_even(num):
    """Returns True if the number is even."""
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() to get only even numbers
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list to display the results
print("Even numbers:", list(even_numbers))

# Example 2: Using filter() with lambda function to filter words longer than 3 letters

words = ["apple", "is", "a", "fruit", "and", "healthy"]

# Lambda function returns True for words with length > 3
long_words = filter(lambda word: len(word) > 3, words)

print("Words longer than 3 letters:", list(long_words))

# Example 3: Filtering out None values from a list

values = [0, None, 5, '', False, 8, None, 3]

# filter(None, iterable) removes all elements that are False in a boolean context
filtered_values = filter(None, values)

print("Filtered (non-false) values:", list(filtered_values))

"""
Summary:
- `filter()` is useful for extracting elements from a collection that meet certain criteria.
- It returns an iterator, so you often need to convert it to a list or tuple to see the results.
"""