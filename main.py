import speech_recognition as sr
import os
import webbrowser
import win32com.client
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error occured, Sorry :("


if __name__ == '__main__':
    print('PyCharm')
    say("Hello, This is Orion A.I. How may I help you? ")
    while True:
        print("Listening....")
        query = takeCommand()

        if "open youtube".lower() in query.lower():
            say("opening Youtube sir..")
            webbrowser.open('https://youtube.com')

        say(query)






