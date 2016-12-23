#!/usr/bin/python


from mutagen.mp3 import MP3

audio = MP3("/opt/DoorbellChimes/HellsBellsChime.mp3")
print int(round(audio.info.length))
