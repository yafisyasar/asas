#Sort List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
##########
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
##########Sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
##############
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#############
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#Sorted
nums = [3, 1, 9, 7, 5]
sorted_nums = sorted(nums)
print(sorted_nums) # Output: [1, 3, 5, 7, 9]
print(nums)        # Output: [3, 1, 9, 7, 5] (original list unchanged)
###############################################
nums = [3, 1, 9, 7, 5]
sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc) # Output: [9, 7, 5, 3, 1]
