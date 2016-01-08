'''
Write a program that prompts the user for a file name, opens this file and reads through the file.
For lines in the form: "X-DSPAM-Confidence:    0.8475", extract the floating point values and compute the average of all of these numbers.
'''

fname = raw_input("Enter file name: ")
fh = open(fname)
numbers = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = float(line[line.find("0."):len(line)+1])
    numbers.append(num)

print 'Average spam confidence:', sum(numbers)/(len(numbers))
