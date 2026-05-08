# Python program to demonstrate
# comparison between the append,extend and insert methods
 
# assign lists
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3]
 
a = [2, 3]
 
# use methods
list_1.append(a)
list_2.insert(1, a)
list_3.extend(a)
 
# display lists
print(list_1)
print(list_2)
print(list_3)
############
fruits=["apple","mango","banana"]
fruits.insert(1,"orange")
print(fruits)
