#!/usr/bin/python
#Pushover code taken from http://www.expertreviews.co.uk/raspberry-pi-foundation/1404017/best-raspberry-pi-projects/page/0/2
#intended mp3 location /opt/DoorbellChimes
#Heavy doorbell chimes at https://github.com/Brockway/DoorbellChimes

import os
import time
import subprocess
import RPi.GPIO as GPIO
import random
import glob
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)

# Parse config.json for configuration options
with open('config.json') as data_file:
    config = json.load(data_file)
mp3location = config['mp3location']

# Alert on start
status = subprocess.call("sudo /opt/pushover.py start", shell=True)
print "Doorbell Server Started\r"
print status

while True:
	if ( GPIO.input(17) == False ):
		chime = random.choice(glob.glob(mp3location+"*.mp3"))
		os.system('date')
		status = subprocess.call("sudo /opt/pushover.py alert", shell=True)
		print "Someone is at the door\r"
		print status
		status = subprocess.call("/usr/bin/mpg123 " +chime, shell=True)
		print status
time.sleep(1)

