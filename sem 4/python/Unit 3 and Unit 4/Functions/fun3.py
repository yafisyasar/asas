# Function with return statement
def greet(name):
	""" This function greet someone."""
	return(name)

str=greet("Ancy")
print(str)
#print(greet("Ancy"))

# Defining a function  
def a_function( string ):  
    '''This prints the value of length of string'''
    return len(string)  
  
# Calling the function we defined  
print( "Length of the string Functions is: ", a_function( "Functions" ) )  
print( "Length of the string Python is: ", a_function( "Python" ) )  

"""
1. A group of related statements that perform a specific task. 
2. It is a block of  organised, reusable code. 
3. It provides better modularity for your application and a high degree of code reusing

def - The keyword ' def ' that marks the start of a function header.

function name - uniquely identifying the function

parameters - to pass values to a function. They are optional.

 :  - to mark the end of the function header

docstring - optional documentation string to describe what the function does.

return - optional  statement.  Used to exit from a function and go back to the place from where it was called. Also used to return a value from a function

__doc__    -   docstring is available to us through print statement through  __doc__ attribute of the function.

 """
