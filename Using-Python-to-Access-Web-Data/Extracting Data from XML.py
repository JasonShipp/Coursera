'''Extracting Data from XML'''

# Import module

import urllib
import xml.etree.ElementTree as ET

# Open socket, connect to web server, turn web page into a file and read its contents

xml_web_file = urllib.urlopen(' http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191261.xml').read()

# Parse the data

parsed_xml = ET.fromstring(xml_web_file)

# Using loops, extract text from within <count> tags from within <comment> tags from within <comments> tags, and append to a list (numbers_list)

numbers_list = []

for top_comment in parsed_xml.findall('comments'):
	for sub_comment in top_comment.findall('comment'):
		number = sub_comment.find('count').text
		numbers_list.append(int(number))

# Sum the numbers in the list
		
sum(numbers_list)



