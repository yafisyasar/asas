# for loop to print all the keys of a dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print("printing all keys...")
for x in Employee:    
    print(x)  
#for loop to print all the values of the dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print("printing all values...")
for x in Employee:    
    print(Employee[x])
    
#for loop to print the values of the dictionary by using values() method.
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print("printing all values using values method...")
for x in Employee.values():    
    print(x)
    
#for loop to print the items of the dictionary by using items() method.
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print("printing all items as tuples in a list...")
y=Employee.items()
print(y)
for x in Employee.items():    
    print(x)
    print(type(x))



