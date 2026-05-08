fruits=["apple","orange","banana","grapes"]
for x in fruits:
    print(x)

#print the characters in a string
fruit="banana"
for x in fruit:
    print(x)

#using break statement in for loop
print("using break first time")
fruits=["apple","orange","banana","grapes"]
for x in fruits:
    print(x)
    if x=="banana":
        break

#using break statement in for loop
print("using break second time")
fruits=["apple","orange","banana","grapes"]
for x in fruits:
    if x=="banana":
        break
    print(x)
#using continue statement in for loop
#skip the rest of the code inside the current iteration of a loop
#and move directly to the next iteration

print("using continue first time")
fruits=["apple","orange","banana","grapes"]
for x in fruits:
    if x=="banana":
        continue
    print(x)

    
 
#using continue statement in for loop
print("using continue second time")
for string in "Python Loops":  
    if string == "o" or string == "p" or string == "t":  
         continue  
    print('Current Letter:', string)














    
    
