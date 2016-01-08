'''
Write a program that prompts the user for a file name, opens this file and reads through the file.
For lines in the form: "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008", extract the hour from the time stamp and build a list of these hours.
Build a dictionary of hours (keys) and counts (values) from the list:
For each hour, check to see if the hour is already in the dictionary; if so, add one to the count; if not, add the hour to the dictionary with a count of 1.
Build a list of tuples, so that each tuple contains an hour-count pair.
Sort this list, and print out each hour-count pair on a new line. 
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours=[]

for line in handle:
    split_line = str(line.split())
    if (split_line).find('From:') >= 0:
        continue
    elif (split_line).find('From') >= 0:
        hour = split_line[(split_line.find(':')-2):(split_line.find(':'))]
        hours.append(hour)
    else:
        continue

distribution = {}

for hour in hours:
    if (str(distribution).find(hour)) >= 0:
        distribution[hour] = distribution[hour] + 1
    else:
        distribution[hour] = 1

dist_list = list()
for key, val in distribution.items():
    dist_list.append((key, val))

dist_list.sort()

for val, key in dist_list: 
    print val, key
