import speech_recognition as sr
import os
import webbrowser
import win32com.client
import openai
import datetime
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error occured, Sorry :("

def openFile():
    files = os.listdir("P:\Songs")



if __name__ == '__main__':
    print('PyCharm')
    say("Hello, This is Orion A.I. How may I help you? ")
    while True:
        print("Listening....")
        query = takeCommand()
        sites = [['youtube', 'https://www.youtube.com'], ['stackoverflow', 'http://stackoverflow.com'],['wikipedia', 'http://wikipedia.org']]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f'opening {site[0]} sir')
                webbrowser.open(site[1])
        # say(query)
        if "time" in query:
            strfTime = datetime.datetime.now().strftime('%H:%M:%S')
            say(f'the time is {strfTime} sir')

        if " open music" in query:
            os.system('')







