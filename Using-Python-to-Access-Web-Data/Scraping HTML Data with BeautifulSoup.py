'''Scraping HTML Data with 'BeautifulSoup' library'''

# Import module

import urllib

# Import http://www.pythonlearn.com/code/BeautifulSoup.py file and save in Python libraries folder ('C:\Anaconda\lib')
# Import BeautifulSoup code

from BeautifulSoup import *

# Open socket, connect to web server, turn web page into a file and read its contents

web_file = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191264.html').read()

# Transform web file into a cleaner version for parsing

web_file_soup = BeautifulSoup(web_file)

# Store a list of the <span> tags found in the web file
 
span_tags = web_file_soup('span')

# Loop over each item in the list, pull out any numbers in the contents of the tags, and append these to a list (numbers_list)

numbers_list = []

for tag in span_tags:
	new_number = re.findall('[0-9]+', tag.contents[0])
	new_number = int(new_number[0])
	numbers_list.append(new_number)
	
# Print the sum of the integers in numbers_list_int
		
print sum(numbers_list)
