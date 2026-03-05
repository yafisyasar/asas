months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    
print("\nPrinting the modified set...");    
print(months)    
print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)    
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.remove("January");    
months.remove("May");    
print("\nPrinting the modified set...");    
print(months)
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving some months from the set...");    
Months.pop();    
Months.pop();    
print("\nPrinting the modified set after pop...");    
print(Months)    
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving all the items from the set...");    
Months.clear()    
print("\nPrinting the modified set...")    
print(Months)    
