# HANNAH VIRTUAL ASSISTANT PROJECT
import clipboard
import winsound
import datetime
import os
import winapps
import psutil
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests
import smtplib
import speech_recognition as sr
import time
import subprocess as sp
import random

import webbrowser as we
from email.message import EmailMessage
# from newsapi import NewsApiClient
# from secrets import senderemail, password
from time import sleep

user = "Ankur"
assistant = "HANNAH"

talk = pyttsx3.init()
t = time.localtime(time.time())
hr = t.tm_hour
min = t.tm_min
CURRENT_TIME = {hr, ":", min}

wake_word_list = ['hannah', 'HANNAH', 'Hannah']
hi_List = ['hi', 'Hi', 'Hello', 'hello', 'Hey', 'hey', 'yo', 'Yo,' 'salam', 'Salam', 'hi ', 'Hi hanah', 'hannah',
           'Hanah']
bye_List = ['Bye', 'bye', 'Goodbye', 'goodbye', 'bye bye', 'Good bye', 'good bye', 'byebye', 'by by', 'By by', 'Tata', 'tata',
            'So long', 'so long', 'okay bye', 'ok bye', 'Ok bye', 'Okay bye']
qst1_list = ["Who are you", 'who are you', 'whats your name',
             'what is your name', 'your name', 'Your name', 'What are you', 'what are you']
res_neg_list = ['bad robot', 'Bad robot', 'bad boy', "Bad boy", 'you are rude Hannah', 'You are rude hannah',
                ' you are a bad robot', 'You are a bad robot']
slang_list = ['Bal', 'bal', 'Crap', 'crap',
              'chutiya', 'Chutiya', 'chootia', 'Chootia']
Love_list = ['i love you', 'I love you', 'Love you', 'love you',
             'Love you hannah', 'love you Hannah', 'i love you hannah', 'I love you hannah']
hate_list = ['i hate you', 'I hate you', 'Hate you', 'hate you']
thank_list = ['thanks', 'thanks hannah', 'thank you', 'thank you hannah',
              'thank you so much hannah', 'Thanks Hannah', 'Thank you Hannah', 'Thank you Hannah']
morning_list = ['good morning', 'very good morning',
                'good morning hannah', 'morning hannah']
evening_list = ['good evening', 'very good evening',
                'good evening hannah', 'evening hannah']
afternoon_list = ['good afternoon',
                  'very good afternoon', 'good afternoon hannah']
friend_list = ['meet my friend', 'meet my new friend']
msg_list = ['send message', 'messsage my friend', 'send message to my friend',
            'send a message', 'send a message to my friend', 'message']
yt_list = ['play', 'open on youtube',
           'open in youtube', 'play on YouTube', 'youtube']
joke_list = ['tell me a joke', 'tell joke', 'tell any joke']
read_list = ['read', 'read selected', 'read what was last copied']
time_list = ['what is the time', 'what time is it',
             'tell time', 'tell me the time']
ss_list = ['take a screenshot', 'screenshot this', 'take a screenshot of this']
quit_list = ['switch off', 'shutdown', 'shut down']
close_list = ['close', 'close this', 'close it']
cam_list = ['open camera', 'launch camera',
            'take a picture', 'click a picture']
storage_list = ['how much memory is used by device',
                'what is storage usage of my device', 'how much memory stored in my laptop']


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 185)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def greet():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        Respond(f"Good Morning {user}")
    elif (hour >= 12) and (hour < 18):
        Respond(f"Good afternoon {user}")
    elif (hour >= 18) and (hour < 21):
        Respond(f"Good Evening {user}")
    elif (hour >= 21) and (hour < 6):
        Respond(f"hello {user}")
    Respond("I am HANNAH. How may I assist you?")


speech = sr.Recognizer()


def Listen():
    listen = str

    with sr.Microphone() as source:
        # beep to inform that it's listening
        winsound.Beep(frequency=2500, duration=100)
        print("listening to you")
        voice = speech.listen(source)
        text = speech.recognize_google(voice)
        print(text)  # print what it heard just to debug

    return text  # return what was heard


def commandlisten():
    listen = str

    with sr.Microphone() as source:
        # beep to inform that it's listening
        winsound.Beep(frequency=2500, duration=100)
        print("what do you wanna listen to")
        talk.say('what do you wanna listen to')
        voice = speech.listen(source)
        text = speech.recognize_google(voice)
        print(text)  # print what it   heard just to debug

    return text  # return what was heard


def Decide(listen):
    """
    Takes decision based on what user says.
    """
    print(f" you = {listen}.")  # just to debug

    # see what user said is in which list or
    if listen in wake_word_list:
        Respond("yes sir, what can i do for you")

    if listen in hi_List:
        Respond("Hi there, Good to see you.")

    elif listen in bye_List:
        print("In bye list.")
        Respond("I liked talking with you, okay take care.")

    elif listen in Love_list:
        SET_LOVE = ["i love you too", "i love you too, but as a friend",
                    "sorry, i have a boyfriend and honestly you deserve someone better.", "love you too"]
        Respond(random.choice(SET_LOVE))

    elif listen in hate_list:
        Respond("Hate you too.")

    elif listen in qst1_list:
        Respond("""I am hannah. your personal assistant""")

    elif listen in res_neg_list:
        Respond("I am very sorry I was just joking.")

    elif listen in slang_list:
        Respond("You are a bad guy")

    elif listen in thank_list:
        Respond("My pleasure sir")

    elif listen in morning_list:
        Respond("very good morning, have a good day sir")

    elif listen in afternoon_list:
        Respond("good afternoon sir")

    elif listen in evening_list:
        Respond("good evening sir")

    elif listen in friend_list:
        Respond("hello buddy...nice to meet you")

    elif listen in yt_list:
        Respond(pywhatkit.playonyt(listen))

    elif listen in joke_list:
        Respond(pyjokes.get_joke())

    elif listen in read_list:
        Respond(clipboard.paste())

    elif listen in time_list:
        Respond({hr, min})

    elif listen in storage_list:
        Respond(psutil.virtual_memory())

    elif listen in msg_list:
        Respond("to whom do you want to send a message")
        mn = +917058983697

        msg = input("record your message")

        pywhatkit.sendwhatmsg("mn", "msg", hr, min)

    elif listen in ss_list:
        Respond("yess boss")
        pyautogui.screenshot(str(time.time()) + ".png").show()

    elif listen in quit_list:
        Respond("SHUTTING DOWN", {os.system("shutdown /s /t 1")})

    elif listen in close_list:
        Respond((input("which app do you want to close?")))

    elif listen in cam_list:
        Respond(
            sp.Popen("C:\Windows\SystemApps\Microsoft.Windows.FileExplorer_cw5n1h2txyewy"))

    elif listen not in msg_list or friend_list or hi_List or bye_List or morning_list or afternoon_list or evening_list or Love_list or hate_list or qst1_list or thank_list or slang_list or res_neg_list:
        Respond("looking for it on google")
        pywhatkit.search(str(listen))

    else:
        Respond("Sorry I don't understand Please say again.")


def Respond(t):
    print(f"HANNAH: {t}")  # to debug and see if everythings going okay

    talk.say(t)
    talk.setProperty('rate', 180)  # 190 words per minute
    talk.runAndWait()


while True:  # for ever loop

    comm = Listen()  # listen to what user says
    Decide(comm)  # take decision and respond
    time.sleep(1)  # after that a delay of 1 second