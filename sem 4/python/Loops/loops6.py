#To print numbers

numbers=[34,12,56,78,23,89,25]
for num in numbers:
    print(num)

#To print sum of numbers
numbers=[1,2,3,4,5]
sums=0
for nums in numbers:
    sums=sums+nums
print(sums)

#To print sum of square of numbers
numbers=[1,2,3,4,5]
sums=0
for nums in numbers:
    sums=sums+nums**2
print(sums)


#Using for else
for x in range(6):
    print(x)
else:
    print("finally finished")

#Using break in for else
for x in range(6):
    if x==3:
        break
    print(x)
else:
    print("finally finished")












    
