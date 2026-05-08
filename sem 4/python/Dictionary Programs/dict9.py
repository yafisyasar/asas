d = {1: 'Amrita', 2: 'Vishwa', 3: 'Vidyapeetham', 'age':25}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)
print(d)
# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
#formatted string literal
#Embed variables or expressions in curly braces {}:
#Python will evaluate these expressions and insert their values into the string.
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)
