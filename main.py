import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS 

def speak(text):
	tts = gTTS(text = text, lang = 'en')
	file_name = "voice.mp3"
	tts.save(file_name)
	playsound.playsound(file_name)

speak('Hello i am Google Assistant')