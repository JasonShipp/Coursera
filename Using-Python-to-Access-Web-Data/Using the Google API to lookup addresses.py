'''Using the Google API to lookup addresses'''

# Import modules

import urllib
import json

# Ask user to input an address

while True:
	address = raw_input('Enter location (or leave blanks to escape): ')
	if len(address) <= 0 : break
	
	# Access the Google address API

	google_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

	# Construct a URL which will look up the user input address in the Google API
	
	google_api_lookup_url = google_api + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving', google_api_lookup_url
	
	# Open and read the JSON data from the URL
	
	google_api_lookup_json = urllib.urlopen(google_api_lookup_url).read()
	
	# Parse the JSON data

	parsed_json = json.loads(google_api_lookup_json)
	
	# Send feedback to user about whether the address lookup has been successful
	
	if 'status' not in parsed_json or parsed_json['status'] != 'OK':
		print 'Failure to retrieve address from Google API - please try another address'
	else:
		print 'API data retrieved:\n'
		print json.dumps(parsed_json, indent=4)
		
		# Print the location, latitude, longitude and place ID from the parsed JSON data
		
		print 'location: ', parsed_json['results'][0]['formatted_address']		
		print 'lat: ', parsed_json["results"][0]["geometry"]["location"]["lat"]
		print 'lng: ', parsed_json["results"][0]["geometry"]["location"]["lng"]
		print 'place ID: ', parsed_json['results'][0]['place_id']	
