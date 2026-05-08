
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nAdding other months to the set...");    
Months.add("July");    
Months.add ("August");    
print("\nPrinting the modified set...");    
print(Months)    
print("\nlooping through the set elements ... ")    
for i in Months:    
    print(i)    
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nupdating the original set ... ")    
Months.update(["July","August","September","October"]);    
print("\nprinting the modified set ... ")     
print(Months)
