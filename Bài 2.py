from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS 

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def speak(text):
	# chuyển hoá text thành voice
	tts = gTTS(text = text, lang = 'en') 
	# Tạo file và lưu lại file voice vừa được chuyển hoá ở trên
	file_name = 'voice.mp3'
	tts.save(file_name)
	# sử dụng hàm playsound trong thư viện playsound với file được truyền vào là file vừa tạo
	playsound.playsound(file_name)

def get_audio():
	# biến r mang giá trị của func Recognizer của thư viện sr(speech_recognition)
	r = sr.Recognizer()
	# chuỗi xử lý
	# function Microphone được gán với biến source
	with sr.Microphone() as source:
		#  biến audio được gán bởi giá trị
		# sr.Recognizer.listen(source)
		# source được gọi lên, fucn sr.Microphone được gọi lên để xác định bật microphone
		# func listen để nhận dữ liệu từ func Microphone vừa được gọi
		# Recognizer nhận dữ liệu từ listen để xử lý là 1 tệp voice
		audio = r.listen(source)

		#audio.save('listen.mp3')
		# tạo biến said
		said = ""

		# Xử lý âm thanh qua try/ except nhằm xử lý các trường hợp sau
		# nếu âm thanh được nhận dạng qua recognizer_google sẽ print
		# nếu âm thanh không có, hoặc âm thanh lỗi, hoặc âm thanh không thể xác định sẽ được trả ra
		# Dưới dạng except để tránh báo lỗi chèn trên hệ thống
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception: " + str(e))

	return said
# Start: google calender API
def main():
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

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()
# End: google calender api

'''text = get_audio()
if "hello" in text:
	speak('Hello, How are you')
elif 'what is your name' in text:
	speak('My name is Chanh')
'''