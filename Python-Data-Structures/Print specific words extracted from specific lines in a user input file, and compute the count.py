'''
Write a program that prompts the user for a file name, opens this file and reads through the file.
For lines in the form: "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008", print out the second word in the line (email addresses).
Print out a count at the end.
'''

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    split_line = line.split()
    if str(split_line).find('From:') >= 0:
        continue
    elif str(split_line).find('From') >=0:        
        print split_line[1]
        count = count + 1
    else:
        continue
        
print "There were", count, "lines in the file with From as the first word"
