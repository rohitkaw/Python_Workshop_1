'''
Given a list, remove the element at index 4 and
add it to the 2nd position and at the end of the list:

'''

list1 = [23, 67, 45, 9, 256, 11, 99]
print("Original List: ", list1)

# Storing the element at index 4 to a variable
var_at_4 = list1[4]

# removing the element at index 4
list1.pop(4)

# inserting the element at 2nd position (i.e, index 1)
list1.insert(1, var_at_4)

# inserting the element at the end of the list
list1.append(var_at_4)

print("After List: ", list1)
