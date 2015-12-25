'''Counting Emails in a Database'''

# Import modules

import sqlite3
import urllib
import re

# Create a connection object to SQLite database

conn = sqlite3.connect("C:/Jason's documents/Training/Using Databases with Python/Databases/database1.sqlite", timeout = 1)

# Create a cursor through which to send commands to the database

cur = conn.cursor()

# Create a new table called 'Counts' (delete any old instances of this table first)

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Ask the user to enter the directory of the file to feed into the database

fname = raw_input('\nPlease enter file directory, or leave blank to use default: ')
if (len(fname) < 1) : fname = "C:/Jason's documents/Training/Using Databases with Python/Data/mbox_data.txt"

# Excluding lines not beginning with "From: ", extract the organisation (domain) of the email address using regular expressions, and store as 'org'

for line in open(fname):
	if not line.startswith('From: '): continue
	org = (re.findall('\S+@(\S+)', line))[0]
	print org
		
	# Run an SQL statement on the database to determine whether the organisation is already in the Counts table 
	
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
	row = cur.fetchone()
	
	# If the first occurrence of the organisation, store it in the Counts table, with a count of '1' 
	
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''', ( org,))
				
	# If the organisation has appeared before, update the relevant row in the Counts table by adding 1 to the count
	
	else: 
		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
			
	# Commit outstanding changes to the Counts table to the disk
	# The program can be made faster by moving the commit so it runs only after the loop completes
	
	conn.commit()
	
# Run an SQL statement to pull the data from the updated Counts table

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 100;'

# Execute the query, and print the results

print "\nCounts:\n"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
