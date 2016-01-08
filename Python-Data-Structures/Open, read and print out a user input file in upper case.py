'''
Write a program that prompts the user for a file name, opens this file, reads through the file, and prints the contents of the file in upper case.
'''

fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.strip()
    print line.upper()
