# Day 10 - Dictionaries

# Creating a dictionary
student = {
    "name": "Edwin",
    "age": 26,
    "country": "Nigeria"
}

print(student)

# Accessing dictionary values
print(student["name"])
print(student["age"])
print(student["country"])

# Changing a value
student["age"] = 27

print(student["age"])

# Adding a new key-value pair
student["city"] = "Lagos"

print(student)

# Deleting a key-value pair
del student["country"]

print(student)

# Looping through dictionary keys
phone = {
    "brand": "Samsung",
    "model": "S10",
    "color": "Black"
}

for key in phone:
    print(key)

# Looping through dictionary values
for value in phone.values():
    print(value)

# Looping through keys and values
for key, value in phone.items():
    print(key, value)

# Final practice
user = {
    "name": "Edwin",
    "age": 26,
    "city": "Lagos"
}

user["age"] = 27
user["country"] = "Nigeria"
del user["city"]

for key, value in user.items():
    print(key, value)