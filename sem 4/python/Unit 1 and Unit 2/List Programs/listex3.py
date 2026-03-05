#clear() removes all elements in the list. It does not take any argument
thislist = [78, "a", 89, "b", "z" , 1, 20, 3, 4, "m" ]
print('thislist before clear:', thislist)
thislist.clear()
print('thislist after clear:', thislist)

# this removes the element on index -2 from the list
         
thislist = [78, "a", 89,  "b", "z" , 1, 20, 3, 4, "m" ]
print(thislist.pop(-2))

#output:
#4                    

# this removes the last element from the list because no argument is passed so
#it will pop the last element from the list

thislist = [78, "a", 89,  "b", "z" , 1, 20, 3, 4, "m" ]
print(thislist.pop())

#output:
#m

# If we provide an argument which is not in the present in the list then it throws an #error IndexError i.e pop index out of range.

thislist = [78, "a", 89,  "b", "z" , 1, 20, 3, 4, "m" ]
print( thislist.pop(-12))


#IndexError: pop index out of range
