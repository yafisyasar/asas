n = int(input("Enter limit: "))

a = 0
b = 1

print("Fibonacci Series:")

while a <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c