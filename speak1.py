#! usr/bin evn python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import time
import playsound
import speech_recognition as sr 
import datetime
from gtts import gTTS 
from datetime import date
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

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
def audio_case():
	time = date.today()
	dateandtime = 'today is:' + str(time)
	speak(dateandtime)

def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service
def get_event(nb_event,service):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print(f'Getting the upcoming {nb_event} evnet')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=nb_event, singleEvents=True,
                                        orderBy='startTime').execute()
    #Bóc mảng iteams từ events_result
    events = events_result.get('items', [])
    # events sẽ chứa rổ hợp tất cả các sự kiện nhận được
    if not events:
        print('No upcoming events found.')
    for event in events:
        # Lấy gía trị cho start bằng cách get từng giá trị tương ứng có trong event
        # event sẽ nhận các key tương ứng với các evnet nhỏ từ evetns
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    # print(events_result)
service = authenticate_google()
get_event(1,service)