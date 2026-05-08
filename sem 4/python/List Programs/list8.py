#######################Del and remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#######################
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
######################
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
######################
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#######################
thislist = ["apple", "banana", "cherry"]
del thislist
#######################The list still remains, but it has no content.
lists = ["apple", "banana", "cherry"]
lists.clear()
print(lists)
