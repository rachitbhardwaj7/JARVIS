import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import random
import webbrowser
import os

engine =pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)
def say(audio):
    engine.say(audio)
    engine.runAndWait()
say("At your service")
say("please Enter Password to open Jarvis ")
for i in range(3):
      
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        say("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        say("Try Again")

from intro import play_gif
play_gif

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening.....") 
        r.pause_threshold =1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
            print("understanding...")
            query = r.recognize_google(audio,language = 'en')  
            print(f"you said :{query}\n")
    except Exception as e:
          print("say that again ")
          return "none"
    return query

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake up" in query:
            say("Hello! How can I assist you?")
        elif "go to sleep" in query:
            say("Okay, you can call me anytime.")
            break
            
        elif "hello" in query:
             say("hello sir, how are you ?")

        elif "i am fine " in query:
             say("that's great sir")
        elif "how are you" in query:
             say("perfect,sir")
        elif " thank you" in query:
             say("you are welcome,sir")
        elif "tired" in query:
            say("Playing your favourite songs, sir")
            a = (1,2,3)  
            b = random.choice(a)
            if b==1:
              webbrowser.open("https://www.youtube.com/watch?v=87K5Uh3AML0")
            if b==2:
                webbrowser.open("https://www.youtube.com/watch?v=87K5Uh3AML0")
            if b==3:
                webbrowser.open("https://www.youtube.com/watch?v=87K5Uh3AML0")
        elif "pause" in query:
              pyautogui.press("k")
              say("video paused")
        elif "play" in query:
          pyautogui.press("k")
          say("video played")
        elif "mute" in query:
         pyautogui.press("m")
         say("video muted")

        elif "volume up" in query:
         from Keyboard import volumeup
         say("Turning volume up,sir")
         volumeup()
        elif "volume down" in query:
         from Keyboard import volumedown
         say("Turning volume down, sir")
         volumedown()
        elif "open" in query:
           from Dictapp import openappweb
           openappweb(query)
        elif "close" in query:
          from Dictapp import closeappweb
          closeappweb(query)
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
           from SearchNow import searchYoutube
           searchYoutube(query)
        elif "wikipedia" in query:
           from SearchNow import searchWikipedia
           searchWikipedia(query)
        elif "temperature" in query:
           search = "temperature in pune"
           url = f"https://www.google.com/search?q={search}"
           r  = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div", class_ = "BNeawe").text
           say(f"current{search} is {temp}")
        elif "weather" in query:
           search = "temperature in delhi"
           url = f"https://www.google.com/search?q={search}"
           r  = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div", class_ = "BNeawe").text
           say(f"current{search} is {temp}")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            say(f"Sir, the time is {strTime}")
        elif "finally sleep" in query:
          say("Going to sleep,sir")
          exit()
        elif "shutdown the system" in query:
          say("Are You sure you want to shutdown")
          shutdown = input("Do you wish to shutdown your computer? (yes/no)")
          if shutdown == "yes":
           os.system("shutdown /s /t 1")
          elif shutdown == "no":
           break
        elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        say("Entering the focus mode....")
                        os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
                        exit()

                    
                    else:
                        pass
        elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()           

        