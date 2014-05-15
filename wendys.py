#!/usr/bin/python

'''
I like Wendy's, I like to know when Wendy's is close by, so I wrote this script to hit their backend API. 

'''

import httplib, json, sys, urllib, pprint
from re import findall

#Simple Usage prompt
if len(sys.argv) != 2:
	print "\nUsage: ./wendys.py <zip code>\n"
	sys.exit(0)

#Define some variables to build the request with
#Convert the given address into a URL friendly format
address = urllib.quote(sys.argv[1])
conn = httplib.HTTPConnection("services.wendys.com")
#May need to update this, if the script breaks
url = "/LocationServices/rest/nearbyLocations?lang=en&cntry=US&sourceCode=WENDYS.COM&version=2.0.0&ts=1400124841164&=&callback=jQuery1710157748194524312_1400124821661&address=" + address + "&radius=10&_=1400124841167"
#connect with a GET
conn.request('GET',url)
resp = conn.getresponse()
body = resp.read()

#now tweak the JSON in the response body, then load it for parsing
json_input = findall("\\((.*?)\\)", body)[0]
decoded = json.loads(json_input)

#Now loop through and print the results! 
for i in decoded['data']:
	print ("\nThere is a Wendy's approximately " + i['distance'] + " miles away located at " + i['address1'] + " in " + i['address2'] + "!")
	print ("Other information:")
	print ("\tPhone Number: " + i['phone'])
	print ("\tLongitude: " + i['lng'])
	print ("\tLatitude: " + i['lat'])
	if i['isOpenLate']:
		print ("\tThis location is open late.")
	else:
		print ("\tSadly, this location is not open late.")
	if i['isOpen24Hours']:
		print ("\tThis location is open 24 hours.")
	else:
		print ("\tSadly, this location is not open 24 hours.")
	print ("\n")
