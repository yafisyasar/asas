n = int(input("Enter limit: "))

a,b=0,1

print("Fibonacci Series:")

while a <= n:
    print(a, end=" ")
    a,b=b,a+b