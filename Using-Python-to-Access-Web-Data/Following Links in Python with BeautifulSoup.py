'''Following Links in Python using 'BeautifulSoup' library'''

# Import module

import urllib

# Import http://www.pythonlearn.com/code/BeautifulSoup.py file and save in Python libraries folder ('C:\Anaconda\lib')
# Import BeautifulSoup code

from BeautifulSoup import *

# Open socket, connect to web server, turn web page into a file and read its contents

web_file = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Brian.html').read()

# Use a loop to clean the web file, list the <a> tags, and read the web file denoted by the 18th <a> tag; repeat 7 times

for loop in range(1, 8,1):
	web_file_soup = BeautifulSoup(web_file)
	a_tags = web_file_soup('a')
	new_link = a_tags[17].get('href', None)
	web_file = urllib.urlopen(new_link).read()
	print new_link
