tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")   
try:   
    del tuple_[3]  
    print(tuple_)  
except Exception as e:  
    print(e)  
print("outside") 
del tuple_  
try:  
    print(tuple_)  
except Exception as e:  
    print(e)  
