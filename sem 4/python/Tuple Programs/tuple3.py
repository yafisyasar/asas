 tuple_ = ("Python", "Tuple", "Ordered", "Collection")
print(tuple_[0])    
print(tuple_[1])    
try:  
    print(tuple_[5])   
except Exception as e:  
    print(e)    
try:  
    print(tuple_[1.0])   
except Exception as e:  
    print(e)  
nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))   
print(nested_tuple[0][3])         
print(nested_tuple[1][1])     








