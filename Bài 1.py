import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS 
import datetime
from datetime import date 
def speak(text):
	# chuyển hoá text thành voice
	tts = gTTS(text = text, lang = 'en') 
	# Tạo file và lưu lại file voice vừa được chuyển hoá ở trên
	file_name = 'voice.mp3'
	tts.save(file_name)
	# sử dụng hàm playsound trong thư viện playsound với file được truyền vào là file vừa tạo
	playsound.playsound(file_name)

#speak('Hello Chanh')
#playsound.playsound('The Chainsmokers - Sick Boy (ESH Remix) [BASS BOOSTED].mp3')
t_today = str(date.today())
#d1 = t_today.strftime('%d/%m/%y')
speak(t_today)
print(t_today)
print(type(t_today))