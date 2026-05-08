#nested for
x = [1, 2]
y = [4, 5]
 
for i in x:
  for j in y:
    print(i, j)


#print multiplication table
# Running outer loop from 2 to 3
 
for i in range(2, 4):
 
    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):
 
        # Printing inside the inner loop
        print(i, "*", j, "=", i*j)
    # Printing inside the outer loop
    print()

#Another example
# Initialize list1 and list2
# with some strings
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'OK']
# Store length of list2 in list2_size
list2_size = len(list2)
 
for item in list1:   
    print("start for loop ")
    i = 0
    while(i < list2_size):
        print(item, list2[i])
        i = i+1
    print("end for loop ")
