Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    
print("Enter the details of the new employee....");    
Employee["Name"] = input("Name: ");    
Employee["Age"] = int(input("Age: "));    
Employee["salary"] = int(input("Salary: "));    
Employee["Company"] = input("Company:");    
print("printing the new data");    
print(Employee)    

#Deleting elements
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    
print("Deleting some of the employee data")     
del Employee["Name"]    
del Employee["Company"]    
print("printing the modified information ")    
print(Employee)    
print("Deleting the dictionary: Employee");    
del Employee    
#print("Lets try to print it again ");    
#print(Employee)    

#Deleting using pop

student = {'name': 'John', 'age': 16, 'grade': 'A'}

# Example 1: Remove an existing key
removed_age = student.pop('age')
print(removed_age)  # Output: 16
print(student)      # Output: {'name': 'John', 'grade': 'A'}

# Example 2: Try to remove a non-existent key with a default value
# Returns "Not Found" without changing the dictionary or raising an error
status = student.pop('city', 'Not Found')
#status = student.pop('city') This gives Key Error
print(status)       # Output: Not Found
print(student)      # Output: {'name': 'John', 'grade': 'A'}

#############################################
student = {'name': 'John', 'age': 16, 'grade': 'A'}

# Remove the last inserted item
last_item = student.popitem()
print(last_item)    # Output: ('grade', 'A')
print(student)      # Output: {'name': 'John', 'age': 16}











