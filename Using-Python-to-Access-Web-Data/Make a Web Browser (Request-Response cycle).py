'''Make a web browser using 'socket' library'''

# Import module

import socket

# Open a new socket

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to web server

new_socket.connect(('www.pythonlearn.com', 80))

# Send a "get data" request to web server

new_socket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

# Using a loop, retrieve and print data from web server in chunks of 1000 characters

while True:
	web_data = new_socket.recv(1000)
	if (len (web_data) <= 0):
		break
	print web_data
	
# Close socket

new_socket.close()


'''Make a web browser using 'urllib' library'''

# Import module

import urllib

# Open socket, connect to web server and turn web page into a file

web_file = urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')

# Print web page header

print web_file.info()

# Use loop to read and print lines in the web file

for line in web_file:
	print line.strip()
