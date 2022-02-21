'''
Write all content of a given file into a
new file by skipping line number 5

check test.txt file and target.txt
'''


# open test.txt file in read mode
file1 = open("c:\\Users\\Administrator\\training.python\\Workshop_1\\test.txt", 'r')
# read the content of the file line by line
content = file1.readlines()
file1.close()

# open other file in write mode
file2 = open("c:\\Users\\Administrator\\training.python\\Workshop_1\\target.txt", 'w')

# Write all content of file1 into a
# new file2 by skipping line number 5(i.e, index 4)
# pass: do nothing and continue the loop
for i in range(0, len(content)):
    if (i == 4):
        pass
    else:
        file2.write(content[i])

# close the file
file2.close()
