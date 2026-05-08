#Pattern Printing
for i in range(1,6):
    for j in range(1,4):
        print("*",end=' ')
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=' ')
    print()




#Using break in for nested loop
for i in range(4):
    for j in range(4):
        if(i==j):
            break
        print(i,j)

#Using continue in for nested loop
first=[2,4,6]
second=[2,4,6]
for i in first:
    for j in second:
        if(i==j):
            continue
        print(i," * ",j," = ",i*j)

#nested while loop
i=1
while(i<=5):
    j=1
    while(j<=10):
        print(j,end=' ')
        j=j+1
    i=i+1
    print()
    
#patterns

rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()


rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

rows=5
num=0
for i in range(rows,0,-1):
    num=num+1
    for j in range(1,i+1):
        print(num,end=' ')
    print()


rows=5
num=6
for i in range(rows,0,-1):
    num=num-1
    for j in range(1,i+1):
        print(num,end=' ')
    print()

