# Python program to show that Python tuples are immutable objects  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", [1,2,3,4])  
  
# Trying to change the element at index 2  
try:  
    tuple_[2] = "Items"  
    print(tuple_)  
except Exception as e:  
    print( e )  
  
# But inside a tuple, we can change elements of a mutable object  
tuple_[-1][2] = 10   
print(tuple_)  
  
# Changing the whole tuple  
tuple_ = ("Python", "Items")  
print(tuple_)  
# Python program to show how to concatenate tuples  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable")  
  
# Adding a tuple to the tuple_  
print(tuple_ + (4, 5, 6))













