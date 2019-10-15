import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS 
from datetime import date

def speak(text):
	tts = gTTS(text = text, lang = 'en')
	file_name = "voice.mp3"
	tts.save(file_name)
	playsound.playsound(file_name)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception: " + str(e))
	return said
def speak_again(text):
	tts = gTTS(text = text, lang = 'en')
	filename = 'voice1.mp3'
	tts.save(filename)
	playsound.playsound(filename)

def audio_case(text):
	time = date.today()
	dateandtime = 'today is:' + str(time)
	speak(dateandtime)
# speak('Hello')
# said_1 = get_audio()
# if 'okay' in said_1:
# 	audio_case(said_1)

help(recognize_google)