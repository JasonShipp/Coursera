'''Load location data from Google API and store in a database'''

# Import modules

import urllib
import sqlite3
import json
import time
import ssl

# Create a connection object to SQLite database

conn = sqlite3.connect("C:/Jason's documents/Training/Using Databases with Python/Databases/geodata.sqlite", timeout = 1)

# Create a cursor through which to send commands to the database

cur = conn.cursor()

# Create new table called Locations (delete any old instances of this table first)

cur.executescript('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)
''')

# Open data file containing location data

file = open("C:/Jason's documents/Training/Using Databases with Python/Data/where.data")

# Loop over each line in the file; each line contains an address

count = 0
for line in file:
    # Optional code to batch loops to 200 a time: if count > 200 : break
	# Clean each address (strip trailing and leading blank spaces)
    address = line.strip()
	
	# Look for the address in the Locations table
    cur.execute("SELECT geodata FROM Locations WHERE address = ?", (buffer(address), ))
    
	# If the address is found, continue to the next loop
    try:
        data = cur.fetchone()[0]
        print 'Address found in database:', address, '\n'
        continue
	# If the address is new, continue within the same loop
    except:
        pass
    print 'Resolving:', address
	
	# Construct a URL which will look up the new address in the Google API 
    url = "http://maps.googleapis.com/maps/api/geocode/json?" + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving API URL:', url
	
	# Open and read the JSON data from the URL, and print the first 20 characters of the JSON
    lookup_json = urllib.urlopen(url).read()
    print 'Retrieved', len(lookup_json), 'characters:', lookup_json[:20].replace('\n',' '), '\n'
    count = count + 1
	
	# Convert the data from Unicode to string, and parse the result; if the result cannot be parsed, continue to the next loop
    try: 
        parsed_json = json.loads(str(lookup_json))
    except: 
        continue
		
    # If the parsed JSON contains a status of 'OK', continue within the same loop; otherwise, print the broken data and continue to the next loop

    if 'status' not in parsed_json or (parsed_json['status'] != 'OK' and parsed_json['status'] != 'ZERO_RESULTS'): 
        print '==== Failure To Retrieve ===='
        print data, '\n'
        continue

	# Input the address and lookup_json into the address and geodata columns of the Locations table
    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES (?, ?)''', (buffer(address),buffer(lookup_json)))
			
	# Commit outstanding database changes to the disk
    conn.commit()
	
print "Run 'Week 5 exercise - geodump.py' to read the data from the database so you can visualise it on a map."
