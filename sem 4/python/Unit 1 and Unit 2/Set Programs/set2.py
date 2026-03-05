set4 = set()
print(set4)
print(type(set4))  
set5 = {1,2,4,4,5,8,9,9,10}  
print("Return set with unique elements:",set5)
lis1 = [ 3, 4, 1, 4, 5 ]
tup1 = (3, 4, 1, 4, 5)
print("The list before conversion is : " ,lis1)
print("The tuple before conversion is : ",tup1) 
print("The list after conversion is : ", set(lis1))
print("The tuple after conversion is : ", set(tup1))
