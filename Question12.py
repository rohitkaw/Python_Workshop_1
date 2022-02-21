'''
Read a file that contains following text.
( see readFile.txt)
Work on following statements:-
-Count the total words in file.
-Count the total number of lines.
-Count the lines start with H.
-Count the frequency of a particular character 'I' or word 'python'.
'''


# open the file to read
file = open("c:\\Users\\Administrator\\training.python\\Workshop_1\\readFile.txt", 'rt')

# 1.Count the total words in file.
data = file.read()
words = data.split()
print("Total words  in File: ", len(words))

# 2.Count the total number of lines.
lines = data.splitlines()
print("total number of lines: ", len(lines))

# 3.Count the lines start with H.
count_lines = 0
for i in lines:
    if(i[0] == 'H'):
        count_lines = count_lines+1

print("Lines that starts with H are: ", count_lines)

# 4.Count the frequency of a particular character 'I' or word 'python'
count_I = 0
count_python = 0
for i in words:
    if(i == 'I'):
        count_I = count_I+1
    elif(i == 'python'):
        count_python = count_python+1

print(F"frequency of 'I' is {count_I} and word 'python' is {count_python}")

file.close()  # closing the file
