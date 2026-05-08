# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()


print('Copied List of prime numbers:', numbers)


# Output: Copied List: [2, 3, 5]
##################
# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

new_list.append('b')
print('Old List:', my_list)
print('Copied List:', new_list)
###############
old_list = [1, 2, 3]

# copy list using =
new_list = old_list


# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)
###################
# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list appending dog
print('Old List:', list)
print('New List:', new_list)
