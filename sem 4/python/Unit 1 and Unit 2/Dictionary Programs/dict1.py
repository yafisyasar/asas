#Creating dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    
# Creating an empty Dictionary   
Dict = {}   
print("Empty Dictionary: ")   
print(Dict)   
  
# Creating a Dictionary   
# with dict() method   
Dict = dict({1: 'Python', 2: 'Programming', 3:'Examples'})   
print("\nCreate Dictionary by using  dict(): ")   
print(Dict)   
  
# Creating a Dictionary   
# with each item as a Pair   
Dict = dict([(1, 'Devansh'), (2, 'Sharma')])   
print("\nDictionary with each item as a pair: ")   
print(Dict)  

#Accessing values
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print("Name : %s" %Employee["Name"])  
print("Age : %d" %Employee["Age"])  
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])








