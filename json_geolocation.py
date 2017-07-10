#!/usr/bin/python
## This programm uses google's geo location api to identify
# the excact location of a specific place
import urllib
import json
serviceurl='http://python-data.dr-chuck.net/geojson?'

while True:
	address= raw_input("Please enter the location:")
	if len(address)<1: break
	url=serviceurl + urllib.urlencode({'sensor':'false','address': address})
	print url
	data_url=urllib.urlopen(url).read()
	try: js_data=json.loads(str(data_url))
	except:js_data=None

	if 'status' not in js_data or js_data['status']!= 'OK':
		print "****Data can not be retrieved****"
		continue
	print json.dumps(js_data, indent=5)

	location_add= js_data['results'][0]['place_id']
	print "The location id of Spiru Haret University is: ", location_add


	print js_data['results'][0]['formatted_address']
