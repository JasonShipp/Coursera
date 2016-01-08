'''
Write a program that prompts the user for a file name, opens this file and reads through the file.
For each line in the file, split the line into a list of words using the split() function.
Build a list of unique words found in the file: for each word in each line, check to see if the word is already in the list; if not, append the word to the list.
'''

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    split_line = line.split()
    for word in split_line:
        if str(lst).find(word) > 0:
            continue
        else:
            lst.append(word)

lst.sort()

print lst
