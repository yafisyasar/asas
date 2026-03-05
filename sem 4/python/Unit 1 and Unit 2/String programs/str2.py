#Slicing
b = "Hello, World!"
print(b[2:5])
#
b = "Hello, World!"
print(b[:5])
#
b = "Hello, World!"
print(b[2:])
#
b = "Hello, World!"
print(b[-5:-2])
#
b = "Hello, World!"
print(b[:-2])
#
b = "Hello, World!"
print(b[-5:])
#
b = "Hello, World!"
print(b[::-1])
#Modify String
a = "Hello, World!"
print(a.upper())
print(a)
#
a = "Hello, World!"
print(a.lower())
#
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#
a = " Hello, World! "
print(a.replace(" ","")) # returns "Hello,World!"
#
a = "Hello, World!"
print(a.replace("H", "J"))
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "He#llo# World!"
print(a.split("#")) # returns ['He','llo', ' World!']
#Merge Strings
a = "Hello"
b = "World"
c = a + b
print(c)
#
a = "Hello"
b = "World"
c = a + " " + b
print(c)
