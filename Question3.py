'''
Write a function function1()
such that it can accept a variable length of
argument and print all arguments value
'''


# accept a variable length of argument
def function1(*Args):
    for i in Args:
        print(i)


function1(5, 15, 25)
