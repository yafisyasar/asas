#list.remove(element)
#removes "banana" from list1
list1 = ["apple", "banana", "cherry"]         
list1.remove("banana")         
print(list1)

#removes first occurrence of 6  from list2
list2 = [1,3,6,9,6,8,4,6]
list2.remove(6)
print(list2)

#remove() returns ValueError when passed object is not present in the list.
list2 = [1,3,6,9,6,8,4,6]
list2.remove(5)
print(list2)
