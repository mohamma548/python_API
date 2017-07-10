#!/usr/bin/python
# retriving XML data using python from the web
import urllib
import xml.etree.ElementTree as ET

url = raw_input("Please enter the url:")
total=0
xml_data=urllib.urlopen(url).read()
tree= ET.fromstring(xml_data)
lst=tree.findall('comments/comment')
# retriving all the numbers inside count tag
for item in lst:
	total= total + int(item.find('count').text)

print "The sum of the numbers inside the count tag are:",total


