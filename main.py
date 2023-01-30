import pyttsx3
import datetime
import speech_recognition as sr
import pyjokes
import webbrowser
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand...")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
#speechtx("hello neelesh")
if __name__=='__main__':

    if "hey peter" in sptext().lower() :
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name="my name is peter "
                speechtx(name)
            elif "how old are you" in data1:
                age="i am 2 years old"
                speechtx(age)
            elif "time" in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "web" in data1:
                webbrowser.open("https://www.google.co.in/")
            elif "linkedin" in data1:
                webbrowser.open("https://www.linkedin.com/in/neelesh-vaishnav-b33619211/")
            elif "geeks for geeks"in data1:
                webbrowser.open("https://auth.geeksforgeeks.org/user/neeleshv689/practice")
            elif "git hub"in data1:
                webbrowser.open("https://github.com/Neeleshvaishnav")
            elif "joke" in data1:
                joke_1=pyjokes.get_joke(language="en",category='neutral')
                print(joke_1)
                speechtx(joke_1)
            elif "exit" in data1:
                speechtx("thank you !")
                break
            time.sleep(5)
    else:
        print("Thanks !")
