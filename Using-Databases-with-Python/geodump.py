'''Pull and normalise location data from a database to a Java file for visualising in HTML'''

# Import modules

import sqlite3
import json
import codecs

# Create a connection object to SQLite database

conn = sqlite3.connect("C:/Jason's documents/Training/Using Databases with Python/Databases/geodata.sqlite", timeout = 1)

# Create a cursor through which to send commands to the database

cur = conn.cursor()

# Select the address and geodata columns from the Locations table
cur.execute('SELECT * FROM Locations')

# Open (in write mode) a Java file to be overwritten
java_file = codecs.open("C:/Jason's documents/Training/Using Databases with Python/Data/where.js", 'w', "utf-8")
java_file.write("myData = [\n")

count = 0

# Loop over each row in the fetched data (stored in 'cur')
for row in cur:
    # Convert the data from Unicode to string, and parse the result; if the result cannot be parsed, continue to the next loop 
    data = str(row[1])
    try: parsed_json = json.loads(str(data))
    except: continue
	
	# If the parsed JSON contains a status of 'OK', continue within the same loop; otherwise, continue to the next loop

    if not('status' in parsed_json and parsed_json['status'] == 'OK'): continue
	
	# Pull the address latitude, longitude and address; if unavailable, continue to the next loop

    lat = parsed_json["results"][0]["geometry"]["location"]["lat"]
    lng = parsed_json["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    formatted_address = parsed_json['results'][0]['formatted_address']
    formatted_address = formatted_address.replace("'","")
	
	# Write the latitude, longitude and address to the 'where.js' file, in the specified format; if not possible, continue to the next loop   
    try :
        print formatted_address, lat, lng

        count = count + 1
        if count > 1 : java_file.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+formatted_address+"']"
        java_file.write(output)
    except:
        continue
	
# Finish writing to the 'where.js' file, close the file and database connections, and print the results 

java_file.write("\n];\n")
cur.close()
java_file.close()
print '\n', count, "records written to where.js"

print '\n', "Open 'Week 5 exercise - where.html' to view the data in a browser"
