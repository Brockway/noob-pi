#!/usr/bin/python
#Pushover code taken from http://www.expertreviews.co.uk/raspberry-pi-foundation/1404017/best-raspberry-pi-projects/page/0/2
#intended mp3 location /opt/DoorbellChimes
#Heavy doorbell chimes at https://github.com/Brockway/DoorbellChimes

import os
import time
import subprocess
import RPi.GPIO as GPIO
import random
import httplib, urllib
import glob
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)

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
mp3location = config['mp3location']
app_key = config['app_key']
user_key = config['user_key']

# Alert on start
PushOver('Doorbell','Started','')
print "Doorbell Server Started\r"

while True:
	if ( GPIO.input(17) == False ):
		chime = random.choice(glob.glob(mp3location+"*.mp3"))
		os.system('date')
		#print chime
		PushOver('Doorbell','Someone is at the door!','')
		#os.system('/usr/bin/mpg321 ' + chime)
		#os.system('/usr/bin/omxplayer -o alsa ' + chime)
		status = subprocess.call("/usr/bin/mpg123 " +chime, shell=True)
		print status
time.sleep(1)

