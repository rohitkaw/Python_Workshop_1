'''
From following two sets find the intersection and remove
those elements from the first set:
'''

set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

# original set
print("Set 1: ", set1)
print("Set 2: ", set2)

# storing intersection in a variable
intersection = set1.intersection(set2)
print("Intersection is: ", intersection)


# removing those elements from the first set
for item in intersection:
    set1.remove(item)

# displaying first set
print(F"First Set after removing common element: {set1}")
