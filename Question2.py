'''
Count the occurrence of each element and create a dictionary to show the count
 of each element.

'''
list2 = [11, 45, 8, 11, 40, 45, 23, 45, 40, 11, 11]

# Creating an empty dictionary first
freq = {}

# using for loop to traverse around the list and count each occurences:
for item in list2:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

print("Element : Count")
for key, value in freq.items():
    print(F"{key} : {value}")
