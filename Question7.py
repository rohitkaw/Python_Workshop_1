'''
How to check file is empty or not

'''

import os
# a file will be empty if its size is 0
# to retreive te size of a file
# we need to use os.path.getsize("path_of_that_file")
filesize = os.path.getsize("c:\\Users\\Administrator\\training.python\\Workshop_1\\sample.txt")

if (filesize == 0):
    print("The file is empty ")
else:
    print("The file is not empty ")
