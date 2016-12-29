#!/usr/bin/python
# Separating pushover out to standalone, get called from sudo from doorbell, can't get rpi to send audio to bluetooth when run as sudo

import sys
import getopt
import httplib, urllib
import json


def PushOver(title,message,url):
	#Connect with the Pushover API server
	conn = httplib.HTTPSConnection("api.pushover.net:443")

	#Send a POST request in urlencoded json
	conn.request("POST", "/1/messages.json",urllib.urlencode({"token": app_key,"user": user_key,"title": title,"message": message,"url": url,}), { "Content-type": "application/x-www-form-urlencoded" })

	#Any error messages or other responses?
	conn.getresponse()

# Parse config.json for configuration options
with open('config.json') as data_file:
    config = json.load(data_file)
app_key = config['app_key']
user_key = config['user_key']
#print app_key
#print user_key

def main(argv):
	var = sys.argv[1]
	#print var
	if var == 'start':
		PushOver('Doorbell','Doorbell has started','')
		print "Doorbell has started\r"
	elif var == 'alert':
		PushOver('Doorbell','Someone is at the door!','')
		print "Someone is at the door!"

if __name__ == "__main__":
	main(sys.argv[1:])
