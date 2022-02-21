'''
11) Write a user function to reverse a string
and list of alphabets or numbers
(without using Python’s reversed or any other inbuilt function).
'''


# user def function
# can accept single string/ List of string/ list of numbers
def reverse(string):
    # checking the parameter is a single string / list
    if(type(string) == str):
        str1 = ""
        for i in string:
            str1 = i + str1
        return str1
    elif(type(string) == list):
        r = []
        for i in string:
            r.insert(0, i)
        return r

single_string = "Python"
list_string = ["Python", "java", "c++"]
list_numbers = [1, 7, 9, 2, 6]

print("Before reversing:", single_string)
print("After reversing:", reverse(single_string))
