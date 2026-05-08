# function with two parameters
def add_numbers(num1, num2):
    sum1 = num1 + num2
    print('Sum: ',sum1)

# function calling
fnum=int(input("Enter the first number :"))
snum=int(input("Enter the second number :"))
add_numbers(fnum,snum)
#add_numbers(3,2)Positional arguments
#add_numbers(num2=3,num1=2)Keyword arguments
