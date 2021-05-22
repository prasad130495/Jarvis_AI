from gtts import gTTS
import speech_recognition as sr
import os
from playsound import playsound
# Need webbrowser to use open webpage functionality 
import webbrowser
# regular expression
import re
from datetime import datetime

def speak(string_to_speak):
    print(string_to_speak)
    if os.path.exists('audio.mp3'):
        os.remove('audio.mp3')
    # Converts text to audio and save it locally as audio.mp3
    tts = gTTS(text=string_to_speak, lang='en')
    tts.save("audio.mp3")
    # Play the saved audio file
    playsound('audio.mp3')
	
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something now!")
        # we will let the microphone to listen for a duration of 5s, you may increase it based on your requirement
        audio = r.record(source,duration=5)
        # Speech recognition using Google Speech Recognition
    speech_to_text = r.recognize_google(audio)
    return speech_to_text


speak("Hi Prasad, what can I do for you?")
recorded_text = listen()
print(recorded_text)
# if you ask to open Mozilla Firefox
if re.findall("Mozilla",recorded_text):
    os.startfile('C://Program Files//Mozilla Firefox//firefox.exe')
    speak("Succesfully opened Mozilla")

# if you ask to open Google Chrome
elif re.findall("Chrome",recorded_text):
    speak("Succesfully opened Chrome")
    os.startfile('C://Program Files//Google//Chrome//Application//chrome.exe')

#if you ask to open my website
elif re.findall("my website",recorded_text.lower()):
    speak("Opening up your website!")
    url = 'https://prasaddev.com'
    webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.get('firefox').open(url)

#if you ask for the current time
elif re.findall("time",recorded_text.lower()):
    now = datetime.now()
    current_time = now.strftime("%H hours %M minutes %S seconds")
    speak("Current Time is " + current_time)

elif re.findall("search for",recorded_text.lower()):
    search = re.sub("search for ","",recorded_text.lower())
    url = str("https://www.google.com/search?q=" + search)
    speak("Searching for" + search)
    webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.get('firefox').open(url)

# Any other condition will require you to update the codes.
else:
    speak("I am not sure what you are asking for. Please redefine in my coding")