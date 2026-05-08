Employee={"Name":"John","Age":29,"Salary":25000,"Company":"GOOGLE","Name":"Kia"}    
for x,y in Employee.items():    
    print(x,y)    

#Keys in a dictionary should be immutable
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100]:"Department ID"}    
for x,y in Employee.items():    
    print(x,y)    
