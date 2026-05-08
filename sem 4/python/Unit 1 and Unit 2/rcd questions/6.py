list1 = [34,10,56,28,10,5,20,32,96,85]
list2 = [18,20]

# a) append and extend
list1.append(list2)
print("After append:", list1)

list1 = [34,10,56,28,10,5,20,32,96,85]
list1.extend(list2)
print("After extend:", list1)

# b) insert 100 at index 9
list1.insert(9,100)
print("After insert:", list1)

# c) sort and sorted
list1.sort()
print("Using sort:", list1)

sorted_list = sorted(list1)
print("Using sorted:", sorted_list)

# d) remove duplicates
unique = list(set(list1))
print("Without duplicates:", unique)

# e) average using sum and len
avg = sum(list1) / len(list1)
print("Average:", avg)

# f) pop, remove, del, clear

list1.pop()
print("After pop:", list1)

list1.remove(10)
print("After remove:", list1)

del list1[2]
print("After del:", list1)

list1.clear()
print("After clear:", list1)