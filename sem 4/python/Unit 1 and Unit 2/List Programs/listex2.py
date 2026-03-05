#python 3 program to demonstrate the use of del() method.
#this deletes the 0th element from the list. 

thislist = [78, "a", 89, "b", "z" , 1, 20, 3, 4, "m" ]
print(thislist)
del thislist[0]
print(thislist)

#output:
#[78, 'a', 89, 'b', 'z', 1, 20, 3, 4, 'm']
#['a', 89, 'b', 'z', 1, 20, 3, 4, 'm']
         

#this deletes the -1th element from the list. 

thislist = [78, "a", 89, "b", "z" , 1, 20, 3, 4, "m" ]
print(thislist)
del thislist[-1]
print(thislist)
#output:
#[78, 'a', 89, 'b', 'z', 1, 20, 3, 4, 'm']
#[78, 'a', 89, 'b', 'z', 1, 20, 3, 4]


#this deletes the element from index 1 to 5(5 excluded) from the list.
       
thislist = [78, "a", 89, "b", "z" , 1, 20, 3, 4, "m" ]
print(thislist)
del thislist[1:5]
print(thislist)
#output:
#[78, 'a', 89, 'b', 'z', 1, 20, 3, 4, 'm']
#[78, 1, 20, 3, 4, 'm']
       
#this delete the  entire list
             
thislist = [78, "a", 89, "b", "z" , 1, 20, 3, 4, "m" ]
print(thislist)
del thislist
print(thislist)
#ouput:

#NameError: name 'thislist' is not defined
#[78, 'a', 89, 'b', 'z', 1, 20, 3, 4, 'm']
