# Python Functions: A Comprehensive Overview

# 1. Defining a simple function
def greet():
    print("Hello, World!")

greet()  # Calling the function

# 2. Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# 3. Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print("Power with default exponent:", power(4))
print("Power with custom exponent:", power(4, 3))

# 4. Function with variable number of arguments (*args)
def print_numbers(*args):
    for num in args:
        print(num, end=' ')
    print()

print_numbers(1, 2, 3, 4)

# 5. Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)

# 6. Returning multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 2, 3, 4, 5])
print("Min:", minimum, "Max:", maximum)

# 7. Lambda (anonymous) functions
square = lambda x: x * x
print("Square of 5:", square(5))

# 8. Nested functions
def outer():
    def inner():
        print("Inside inner function")
    print("Inside outer function")
    inner()

outer()

# 9. Function documentation (docstring)
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b

print(multiply.__doc__)

# 10. Function as first-class objects (passing functions as arguments)
def apply_func(func, value):
    return func(value)

print("Applying square to 6:", apply_func(square, 6))

# 11. Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))