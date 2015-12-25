'''Multi-Table Database - Tracks'''

# Import modules

import xml.etree.ElementTree as ET
import sqlite3

# Create a connection object to SQLite database

conn = sqlite3.connect("C:/Jason's documents/Training/Using Databases with Python/Databases/musicdb.sqlite", timeout = 1)

# Create a cursor through which to send commands to the database

cur = conn.cursor()

# Create new tables (delete any old instances of these table first)

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
	rating INTEGER,
	count INTEGER
);
''')

# Ask the user to enter the directory of the XML file to feed into the database

fname = raw_input('\nPlease enter file directory, or leave blank to use default: ')
if (len(fname) < 1) : fname = "C:/Jason's documents/Training/Using Databases with Python/Data/music_library.xml"

# Define a function to return the information text contained within specific tags within specific dictionaries

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def lookup(dict, info_tag):
    found = False
    for child in dict:
        if found : return child.text
		# If the tag within the dictionary is a "key" tag and the information it holds matches the field being searched for, set "found" to True, and return the information in the next tag (on the next loop)
		# Else return nothing
        if child.tag == 'key' and child.text == info_tag:
            found = True
    return None

# Open and parse the XML file

parsed_xml = ET.parse(fname)

# Find all the dictionaries within dictionaries within dictionaries, and print the number of these

all_dicts = parsed_xml.findall('dict/dict/dict')
print 'Dict count:', len(all_dicts)

# Excluding dictionaries beginning with "Track ID" tags, apply the lookup function for specific fields

for dict in all_dicts:
    if (lookup(dict, 'Track ID') is None): continue

    name = lookup(dict, 'Name') 
    genre = lookup(dict, 'Genre')
    artist = lookup(dict, 'Artist')
    album = lookup(dict, 'Album')
    count = lookup(dict, 'Play Count')
    rating = lookup(dict, 'Rating')
    length = lookup(dict, 'Total Time')
	
	# Skip dictionaries with specific missing fields

    if name is None or artist is None or album is None: continue
		
	# Print the returned information

    print name, artist, album, count, rating, length
	
	# Insert the artist into the name column of the Artist table; if the artist already exists in the table, do not insert it
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
		VALUES ( ? )''', (artist,))
	# Extract the id of the artist for inputting into the artist_id column of the Album table
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
	
	# Insert the genre into the name column of the Genre table; if the genre already exists in the table, do not insert it
    cur.execute('''INSERT OR IGNORE INTO Genre (name)
		VALUES ( ? )''', (genre,))
	# Extract the id of the genre for inputting into the genre_id column of the Track table
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    try:
        genre_id = cur.fetchone()[0]
    except TypeError:
        continue
		
	# Insert the album and artist_id into the title and artist_id columns of the Album table; if the album already exists in the table, do not insert it
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
		VALUES ( ?, ? )''', (album, artist_id))
	# Extract the id of the album for inputting into the album_id column of the Track table
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
		
	# Insert the name, album_id, genre_id, length, rating and count into the title, album_id, genre_id, len, rating, count columns of the Track table;
	# If the track already exists in the table, overwrite it
    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
		VALUES ( ?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))
		
	# Commit outstanding database changes to the disk

    conn.commit()
