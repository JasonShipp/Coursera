'''
Write a program that prompts the user for a file name, opens this file and reads through the file.
For lines in the form: "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008", record the second word in the line (email addresses).
Build a dictionary of email addresses (keys) and counts (values) found in the file:
For each email address, check to see if the email is already in the dictionary; if so, add one to the count; if not, add the email to the dictionary with a count of 1.
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dictionary = {}
max = 0
max_address = None

for line in handle:
    split_line = line.split()
    if (str(split_line).find('From') >= 0) and not (str(split_line).find('From:') >= 0):
        address = split_line[1]
        if str(dictionary).find(address) >= 0:
            dictionary[address] = dictionary[address] + 1
        else:
            dictionary[address] = 1
    else:
        continue
        
for entry in dictionary:
    if dictionary[entry] > max:
        max = dictionary[entry]
        max_address = entry
        
print max_address, max
