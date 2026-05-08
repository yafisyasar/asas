# Python program to show repetition in tuples  
    
tuple_ = ('Python',"Tuples")  
print("Original tuple is: ", tuple_)

  
# Repeting the tuple elements  
tuple_ = tuple_ * 3  
print("New tuple is: ", tuple_)  

# Python program to show how to use tuple methods (.index() and .count()) work  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")  
  
# Counting the occurrence of an element of the tuple using the count() method  
print(tuple_.count('Ordered'))  
  
# Getting the index of an element using the index() method  
print(tuple_.index('Ordered')) # This method returns index of the first occurrence of the element

