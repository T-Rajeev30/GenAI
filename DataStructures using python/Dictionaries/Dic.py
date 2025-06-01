# Python Dictionary Tutorial: Learn Everything About Dictionaries

# 1. Creating Dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 25, "city": "New York"}
mixed_keys = {1: "one", (2, 3): "tuple as key"}

# 2. Accessing Values
print(person["name"])           # Access by key
print(person.get("age"))        # Safe access

# 3. Adding and Modifying
person["email"] = "alice@example.com"  # Add new key-value
person["age"] = 26                     # Modify value
print(person)

# 4. Removing Items
del person["city"]                 # Remove by key
removed = person.pop("email")      # Remove and return value
print(person, removed)

# 5. Dictionary Functions
print(len(person))                 # Number of items
print(list(person.keys()))         # All keys
print(list(person.values()))       # All values
print(list(person.items()))        # All key-value pairs

# 6. Checking Existence
print("name" in person)            # Check if key exists
print("city" not in person)

# 7. Iterating
for key in person:
    print(key, person[key])
for key, value in person.items():
    print(key, value)

# 8. Copying Dictionaries
copy1 = person.copy()
copy2 = dict(person)
print(copy1, copy2)

# 9. Nested Dictionaries
students = {
    "A": {"name": "Bob", "age": 20},
    "B": {"name": "Carol", "age": 22}
}
print(students["A"]["name"])

# 10. Dictionary Comprehensions
squares = {x: x**2 for x in range(5)}
print(squares)

# 11. Clearing Dictionary
person.clear()
print(person)
