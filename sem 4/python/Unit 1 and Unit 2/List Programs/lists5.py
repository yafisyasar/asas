#A program to remove the duplicate element of the list
list1 = [1,2,2,3,55,98,65,65,13,29]  
# Declare an empty list that will store unique values  
list2 = []  
for i in list1:  
    if i not in list2:  
        list2.append(i)  
print(list2)  

#A program to find the sum of elements in a list
list1 = [3,4,5,9,10,12,24]  
sum = 0  
for i in list1:  
    sum = sum+i      
print("The sum is:",sum)  


#To check whether the lists contain any common element
list1 = [1,2,3,4,5,6]  
list2 = [7,8,9,2,5]  
for x in list1:  
    for y in list2:  
        if x == y:  
            print("The common element is:",x)







            
