'''
Nested function:
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate
the addition of a and b
At last, an outer function will add 5 into addition and return it
'''


def function1(a, b):            # outer function
    def function2(x, y):        # inner Function
        return x+y              # returns the sum of the two parameters
    result = function2(a, b)+5  # variable result storing the returned value+5
    return result               # returning the final result

print(function1(25, 7))         # calling outer functn and printing its result
