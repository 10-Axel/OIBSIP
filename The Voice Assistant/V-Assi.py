# -*- coding: utf-8 -*-
"""
Created o Aug 10 2024 

@author: TIKENDRA
"""


import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import requests
import shutil
import ctypes
import wolframalpha
from ecapture import ecapture as ec

assname="Vaassi"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

#text to speech
def speak(audio) :
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice to text
'''def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return takecommand()  # Recursively call takecommand() to retry
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            speak("Sorry! Can you repeat please...")
            return ""     '''
    
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio =  r.listen(source,timeout=5 ,phrase_time_limit=10)#
        except sr.WaitTimeoutError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return takecommand()  # Recursively call takecommand() to retry

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query

    except Exception as e:
        speak("Sorry! can you repeat please...")
        return ""  # Return an empty string instead of None

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Mr. TK")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Mr. TK")
    elif hour>=16 and hour<20:
        speak("Good Evening Mr. TK")
    else:
        speak("Good Night Mr. TK")

    strTime = datetime.datetime.now()  
    formatted_date = strTime.strftime("%d %B %Y, %A.")
    speak(f"Today is {formatted_date}")
    formatted_time = strTime.strftime("%I:%M %p")
    
    speak(f"And It's {formatted_time}")
    speak("I am Vaassi, How can I help you sir?")

def news():
    main_url= "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=3291b5209929453889e620722ce972ee"

    main_page = requests.get(main_url).json()
    #print (main_page)
    articles = main_page["articles"]
    #print (articles)
    head = []
    desc = []
    day = ["first","second","third","fourth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
        desc.append(ar["description"])

    speak("today's news are: ")

    for i in range (len(day)):
        print(f"today's news are: ",head[i])
        speak(f" {head[i]}")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img.save('')     # Location=Your screenshots saving file location

def username():
    speak("Sure Sir,")
    speak("What should i call you sir")
    uname = takecommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    #print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    #print("#####################".center(columns))
     
    speak("How can i Help you, Sir")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wish()
    
    while True:
    #if 1:
        
        query = takecommand().lower()


        if "open notepad" in query:
            speak("Opening Notepad")
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "switch user" in query:
            username()

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change your name" in query:
            speak("What would you like to call me, Sir ")
            assname = takecommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Teekendra.")

        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takecommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep yourself' in query:
            sys.exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'stands for' in query: 
            speak('V-Assi stands for Virtual Assistant.')   

        elif "play some music" in query:
            music_dir = "C:\\Users\\Tikendra Pal\\Music\\Songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            #for song in songs:
            #    if song.endswith('.m4a'):
            os.startfile(os.path.join(music_dir,  rd))
    
        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia ")
            speak(results)
            #print(results)

        elif "open youtube" in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("www.youtube.com")

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif "open google" in query:
            speak("Sir, what do you want to search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+91**********", "Your Message...",0,34)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again ")   

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "set alarm" in query:
            speak("at what time sir?")
            alm = takecommand().lower()
            nn = int(datetime.datetime.now().hour)
            if nn==alm:
                music_dir = "C:\\Users\\Tikendra Pal\\Music\\Songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[36]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("restart /r /t 5")        

        elif "turn on sleep mode of the window" in query:
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")    

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif "tell me the news" in query:
            speak("please wait sir, fetching the news...")
            news()
        
        elif "calculate" in query: 
                    
                    app_id = "U8Y8V7-AK8K8KY8J5"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('calculate') 
                    query = query.split()[indx + 1:] 
                    res = client.query(' '.join(query)) 
                    answer = next(res.results).text
                    print("The answer is " + answer) 
                    speak("The answer is " + answer)

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "C:\\Users\\Tikendra Pal\\Pictures\\Acer",
                                                       0)
            speak("Background changed successfully")

        elif "take a picture" in query:
            ec.capture(0, "Camera", "img.jpg")

        #speak("Do you need any other help, I am here at your service")

