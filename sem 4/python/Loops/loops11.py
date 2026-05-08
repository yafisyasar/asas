# Python program to demonstrate
# difference between pass and 
# continue statements

for i in range(5):
    if i == 2:
        continue  # Skip iteration when i is 2
    print("This is iteration", i)



for i in range(10):
    if i == 7:
        pass  # This loop does nothing when i is 7
    else:
        print("This is iteration", i)
