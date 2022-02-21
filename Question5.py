'''
Display “Pandemic will end soon” as “Pandemic$$will$$end$$soon”
using output formatting of a print() function
'''

var_string = "Pandemic{}will{}end{}soon"

print("Before: ", var_string.format(" ", " ", " "))
print("After: ", var_string.format("$$", "$$", "$$"))
