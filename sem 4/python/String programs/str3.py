#This is wrong
'''
age = 36
txt = "My name is John, I am " + age
print(txt)


But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
'''
#Using format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#













