Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)    

Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)    
set1 = {1,2,3, "hello", 20.5, 14}  
print(type(set1))  
try:
    set2 = {1,2,3,["hello",4]}  
    print(type(set2))
except Exception as e:
    print(e)
