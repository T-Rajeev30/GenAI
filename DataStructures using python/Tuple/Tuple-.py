# 1. Introduction to Tuples
# A tuple is a collection of ordered, immutable, and heterogeneous elements in  . It's similar to a list, but tuples cannot be changed after creation.
example = (1, "apple", 3.14)
print(example)  # Output: (1, 'apple', 3.14)
# 2. Creating Tuples
# You can create tuples using parentheses () or without them (tuple packing):
t1 = (1, 2, 3)
t2 = 4, 5, 6  # Tuple without parentheses
t3 = tuple([7, 8, 9])  # Using tuple() constructor
print(t1, t2, t3)
# Special case: Single-element tuple must have a comma 
t = (5,)  # Correct
not_a_tuple = (5)  # This is just an integer
# 3. Accessing Tuple Elements
# Use indexing and slicing: 
t = ('a', 'b', 'c', 'd')
print(t[0])      # Output: 'a'
print(t[-1])     # Output: 'd'
print(t[1:3])    # Output: ('b', 'c')
# 4. Tuple Operations
# Tuples support:
# Concatenation: +
# Repetition: *
# Membership testing: in
# Iteration: for loop
a = (1, 2)
b = (3, 4)
print(a + b)     # (1, 2, 3, 4)
print(a * 2)     # (1, 2, 1, 2)
print(2 in a)    # True
for i in a:
    print(i)
# 5. Immutable Nature of Tuples
# Tuples cannot be modified (no item assignment or deletion): 
t = (1, 2, 3)
# t[0] = 10  # ❌ Error: 'tuple' object does not support item assignment
# However, if a tuple contains a mutable object (like a list), the object can be modified:
t = (1, [2, 3])
t[1][0] = 99
print(t)  # (1, [99, 3])
# 6. Tuple Methods
# Tuples support only two methods: 
 
t = (1, 2, 3, 2, 2)
print(t.count(2))  # 3
print(t.index(3))  # 2
# 7. Packing and Unpacking Tuples
# Packing: Combining values into a tuple
# Unpacking: Extracting values from a tuple

# Packing
packed = (10, 20, 30)

# Unpacking
a, b, c = packed
print(a, b, c)  # 10 20 30
# Use * to unpack remaining items:
a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]
# 8. Nested Tuple
# Tuples can contain other tuples or collections:
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1])      # (3, 4)
print(nested[1][0])   # 3
# 9. Practical Examples and Common Errors
# ✅ Practical Use Case: Returning multiple values from a function

def min_max(nums):
    return min(nums), max(nums)

result = min_max([1, 2, 3, 4])
print(result)  # (1, 4)
# ❌ Common Errors
# Modifying tuple:
t = (1, 2, 3)
# t[1] = 9  # ❌ TypeError
# Forgetting comma in single-item tuple:
x = (5)      # Not a tuple, just int
y = (5,)     # ✅ Tuple
