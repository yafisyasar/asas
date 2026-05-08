
Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2)

Days1 = {"Monday","Tuesday","Wednesday","Thursday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1.union(Days2))
Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2)
set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2)) 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print("intersection_update")
print(x)
print(y)

a = {"Devansh", "bob", "castle"} 
b = {"castle", "ria", "bob"}    
c = {"fusion", "bob", "castle"}    

a.intersection_update(b,c)

print(a)
print(b)
print(c)
b.intersection_update(c)
print(b)





