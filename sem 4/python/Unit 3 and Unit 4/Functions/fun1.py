#function demo for greeting
def greet(n):
    '''This function performs greeting action.''' #docstring
    print("Hello " + n + ", Good Morning")
    
    
n1=input("Enter a name :")
greet(n1)
print(greet.__doc__) # giving out the documentation string at runtime


