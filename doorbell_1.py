#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO
import random
import httplib, urllib
from mutagen.mp3 import MP3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)

def PushOver(title,message,url):
	app_key = "Your App Key Here"
	user_key = "Your User Key Here"
	#Connect with the Pushover API server
	conn = httplib.HTTPSConnection("api.pushover.net:443")

	#Send a POST request in urlencoded json
	conn.request("POST", "/1/messages.json",urllib.urlencode({"token": app_key,"user": user_key,"title": title,"message": message,"url": url,}), { "Content-type": "application/x-www-form-urlencoded" })

	#Any error messages or other responses?
	conn.getresponse()

# Alert on start
PushOver('Doorbell','Started','')
print "Doorbell Server Started\r"

while True:
	if ( GPIO.input(17) == False ):
		while True:
			filename = random.choice(os.listdir("/opt/DoorbellChimes"))
	        	if ( filename.endswith(".mp3") ):
				break
		chime = '/opt/DoorbellChimes/' + filename
		os.system('date')
		#print chime
		os.system('/usr/bin/mpg321 ' + chime)
		PushOver('Doorbell','Someone is at the door!','')
		
time.sleep(1)
