'''Many Students in Many Courses'''

# Import modules

import json
import sqlite3

# Create a connection object to SQLite database

conn = sqlite3.connect("C:/Jason's documents/Training/Using Databases with Python/Databases/courses_users.sqlite", timeout = 1)

# Create a cursor through which to send commands to the database

cur = conn.cursor()

# Create new tables (delete any old instances of these table first)

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Ask the user to enter the directory of the XML file to feed into the database

fname = raw_input('\nPlease enter file directory, or leave blank to use default: ')
if (len(fname) < 1) : fname = "C:/Jason's documents/Training/Using Databases with Python/Data/roster_data.json"

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],...

# Open and parse the JSON file

json_data = open(fname).read()
parsed_json = json.loads(json_data)

# Store and print the entry values

for entry in parsed_json:

	name = entry[0];
	title = entry[1];
	role = entry[2];

	print name, title, role
	
	# Insert the name into the name column of the User table; if the name already exists in the table, do not insert it
	cur.execute('''INSERT OR IGNORE INTO User (name) 
		VALUES ( ? )''', (name, ))
	# Extract the id of the name for inputting into the user_id column of the Member table
	cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
	user_id = cur.fetchone()[0]
	
	# Insert the title into the title column of the Course table; if the title already exists in the table, do not insert it
	cur.execute('''INSERT OR IGNORE INTO Course (title) 
		VALUES ( ? )''', (title, ))
	# Extract the id of the title for inputting into the course_id column of the Member table
	cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
	course_id = cur.fetchone()[0]
	
	# Insert the user_id, course_id and role into the user_id, course_id and role columns of the Member table;
	# If the row already exists in the table, overwrite it
	cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
		VALUES (?, ?, ?)''', (user_id, course_id, role))
	

# Commit outstanding database changes to the disk

conn.commit()
