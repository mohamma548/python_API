#!/usr/bin/python
# Accessing web data using json API
# This programme calculates the sum of all accounts from a web_data using json
import urllib
import json
url= raw_input('Please enter the url:')
data= urllib.urlopen(url).read()
total=0
print "Retriving", url
#print data
j_data=json.loads(data)
print "length", len(j_data["comments"])

for item in j_data["comments"]:

	total=total + int (item["count"])

print "The sum of all counts are: ",total


