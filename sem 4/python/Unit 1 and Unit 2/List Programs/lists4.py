#Iterating a list
lists = ["John", "David", "James", "Jonathan"]    
for i in lists:   
    print(i)  
#Program to add elements to the list and display them
l =[]  
n = int(input("Enter the number of elements in the list:"))  
for i in range(0,n):     
    l.append(input("Enter the item:"))     
print("printing the list items..")   
for i in l:   
    print(i, end = "  ")     
#Removing ellements from the list
lists = [0,1,2,3,4]     
print("\nprinting original list: ");    
for i in lists:    
    print(i,end=" ")    
lists.remove(2)#removes item    
print("\nprinting the list after the removal of element...")    
for i in lists:    
    print(i,end=" ")
#########################
#print()
print("Using break and else in for loop")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#########################
for x in range(6):
  if x == 3:
      break
  print(x)
else:
  print("Finally finished!")

