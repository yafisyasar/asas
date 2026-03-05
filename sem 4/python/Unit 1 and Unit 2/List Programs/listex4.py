#append method
#It adds an element at the end of the list. The argument passed in the append
#function is added as a single element at end of the list and
#the length of the list is increased by 1.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert(index,element)
#This method can be used to insert a value at any desired position.
#It takes two arguments-element and the index at which the element has to be inserted.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#extend method
#This method appends each element of the iterable (tuple, string, or list)
#to the end of the list and increases the length of the list by
#the number of elements of the iterable passed as an argument.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist.append(tropical)
print(thislist)

#Another example
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3]
 
a = [2,3]
 
# use methods
list_1.append(a)
list_2.insert(2, a)
list_3.extend(a)
 
# display lists
print(list_1)
print(list_2)
print(list_3)

#output
#[1, 2, 3, [2, 3]]
#[1, 2, 3, [2, 3]]
#[1, 2, 3, 2, 3]
