import pyttsx3
import datetime
engine =pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)
def say(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<= 12:
      say("good morning sir")
    elif hour>12 and hour <=18:
      say("good afternoon sir")
    else:
       say("good evening,sir")

    say("please tell me,how can i help you")