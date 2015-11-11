# Import modules

import re
import urllib2

# Open the assignment text file from its URL

data = urllib2.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/regex_sum_191259.txt')

# Loop over each line in the file, and append any numbers to a list (numbers_list_str)

numbers_list_str = []
for line in data:
	new_numbers = (re.findall('[0-9]+', line))
	numbers_list_str.extend(new_numbers)
	
# Loop over each item in the list, convert to an integer, and append to a new list (numbers_list_int)
	
numbers_list_int = []	
for number in numbers_list_str:
	numbers_list_int.append(int(number))
	
# Print the sum of the integers in numbers_list_int
		
print sum(numbers_list_int)
