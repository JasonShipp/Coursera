'''Extracting Data from JSON'''

# Import modules

import urllib
import json

# Open socket, connect to web server, turn web page into a file and read its contents

json_web_file = urllib.urlopen(' http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191265.json').read()

# Parse the data

parsed_json = json.loads(json_web_file)

# Using a loop, extract text from within <count> tags from within dictionary entries from within <comments> tags, and append to a list (numbers_list)

numbers_list = []

for item in range(0, len(parsed_json['comments']), 1):
	number =  parsed_json['comments'][item]['count']
	numbers_list.append(int(number))
	
# Sum the numbers in the list	

sum(numbers_list)
