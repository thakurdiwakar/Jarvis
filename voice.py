import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit

from selenium import webdriver
import time
import requests
import subprocess
from datetime import date
import calendar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
cdriver = 'C:\\Users\\diwakar singh\\Downloads\\chromedriver'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Default voice, you can change the index to choose a different voice

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!, Sir")
        speak("Good Morning!, Sir")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon!, Sir.. ")
        speak("Good Afternoon!, Sir.. ")

    else:
        print("Good Evening!, Sir")
        speak("Good Evening!, Sir")

    print("I am Jarvis, The AI Assistant of Diwakar ... How can i help you...!  ")
    speak("I am  Jarvis, The AI Assistant of, Diwakar... How can i help you...!  ")


def changeVoice():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    
    print("Available voices:")
    for i, voice in enumerate(voices):
        print(f"{i+1}. {voice.name}")
    
    print("Choose a voice by typing the corresponding number:")
    selected_voice_index = int(input())
    
    if 1 <= selected_voice_index <= len(voices):
        engine.setProperty('voice', voices[selected_voice_index - 1].id)
        print("Voice changed successfully!")
    else:
        print("Invalid voice selection. No changes made.")






def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('diwakr@student.iul.ac.in', sst)
    server.sendmail('diwakr@student.iul.ac.in', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    cmd = 1
    while cmd:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.strip()
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'change voice' in query:
         changeVoice()
   
        elif 'quit' in query or 'exit' in query or 'keep quiet' in query or 'good night' in query:
            if 'good night' in query:
                hour = int(datetime.datetime.now().hour)
                if (hour >= 21 and hour < 24) or (hour >= 0 and hour <= 2):
                    print("Ok sir, Good Night.. I am always with you sir, bye, Take care..")
                    speak("Ok sir, Good Night.. I am always with you sir, bye, Take care..")
                    cmd = 0
                else:
                    print("No sir.. Don't make me a fool... ")
                    speak("No sir.. Don't make me a fool... ")
            else:
                print("Ok sir.. I hope, I did well, bye sir, Take care..")
                speak("Ok sir.. I hope, I did well, bye sir, Take care..")
                cmd = 0

        elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")
            elif hour >= 12 and hour < 18:
                print("Good Afternoon! sir...")
                speak("Good Afternoon! sir...")
            elif hour >= 18 and hour < 24:
                print("Good evening sir..")
                speak("Good evening sir..")

        elif 'play' in query:
            query = query.replace("play", "")
            query = query.replace("search", "")
            kit.playonyt(query)
            print(f"Playing, {query}")
            speak(f"Playing, {query}")

        elif 'open google' in query:
            print("Opening Google....")
            speak("Opening Google....")
            url = "google.com"
            webbrowser.get(chrome_path).open(url)

        elif 'google' in query:
            query = query.replace("in", "")
            query = query.replace("on", "")
            query = query.replace("google", "")
            query = query.replace("search", "")
            tab = "http://google.com/?#q="
            webbrowser.open(tab + query)
            speak("Result on your screen")

        elif 'open gmail' in query:
            speak("Ok sir, opening Gmail")
            webbrowser.open("www.gmail.com")
            speak("Gmail on your screen, Sir...")

        elif 'open facebook' in query:
            print("Opening Facebook....")
            speak("Opening Facebook....")
            url = 'www.facebook.com'
            speak("Facebook on your screen, Sir...")
            webbrowser.get(chrome_path).open(url)

        elif 'open whatsapp' in query:
            print("Opening WhatsApp....")
            speak("Opening WhatsApp....")
            url = 'web.whatsapp.com'
            speak("WhatsApp on your screen, Sir...")
            webbrowser.get(chrome_path).open(url)

        elif 'show my last' in query:
            file = open("pywhatkit_dbs.txt", "r", encoding='utf-8')
            content = file.read()
            file.close()
            if content == "--------------------":
                content = None
            print(content)
            speak(content)

        elif 'open control' in query:
            print("Opening Control Panel....")
            speak("Opening Control Panel....")
            subprocess.call('control.exe')
            speak("Control Panel on your screen, Sir...")

        elif 'open file' in query:
            speak("Opening File Explorer")
            subprocess.call('explorer.exe')
            speak("File explorer on your screen, Sir...")

        elif 'music' in query or 'gana' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print("Ok Sir, Playing music....")
            speak("Ok Sir, Playing music....")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'open visual studio' in query or 'open vs code' in query:
            codePath = "C:\\Users\\SBK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'about' in query:
            print('Hello sir, I am Lucy, developed by Diwakar and guided by Mr. Ayaz Sir')
            speak('Hello sir, I am Lucy, developed by Diwakar and guided by Mr. Ayaz Sir')

        elif 'date' in query:
            today = datetime.datetime.now()
            today1 = today.strftime("%d, %B, ")
            rr = str(today.year)
            today1 = today1 + rr
            print("Today's date is...")
            print(today1)
            speak("Today's date is...")
            speak(today1)

        elif 'today' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")
            elif hour >= 12 and hour < 18:
                print("Good Afternoon! sir...")
                speak("Good Afternoon! sir...")
            elif hour >= 18 and hour < 24:
                print("Good evening sir..")
                speak("Good evening sir..")

            today = datetime.datetime.now()
            today1 = today.strftime("%d, %B, ")
            rr = str(today.year)
            today1 = today1 + rr
            print("Today's date is...", today1)
            speak("Today's date is..." + today1)
            date = date.today()
            st = calendar.day_name[date.weekday()]
            print("Today is ", st)
            speak("Today is " + st)

        elif 'day' in query:
            date = date.today()
            st = calendar.day_name[date.weekday()]
            speak("Today is " + st)
            print("Today is ", st)

        elif 'send email' in query:
            try:
                speak("Give the Name of Reciever.")
                dic = {
                    "Suraj": "s@xyz.com",
                    "Bhanu": "bh@xyz.com",
                    "Diwakar": "ds6228353@gmail.com",
                    "Ayush": "ay@xyz.com",
                    "Rahul": "ka@xyz.com",
                }

                to = takeCommand()
                to = dic[to]
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak(f"Email has been sent to {to}, Thank you....")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif 'who are you' in query or 'your name' in query:
            print('I am AI Based Lucy, the assistant of Diwakar...')
            speak('I am AI Based Lucy, the assistant of Diwakar...')

        elif 'favourite song' in query:
            speak("My favorite song is 'Megenta Riddim'. Do you want to play?")
            query = takeCommand().lower()
            if 'yes' in query or 'yah' in query:
                url = 'https://www.youtube.com/watch?v=op4B9sNGi0k'
                speak("Playing My Favorite song")
                webbrowser.get(chrome_path).open(url)
            else:
                speak("Ok sir, no problem")

        elif 'open turbo c' in query:
            speak("Opening Turbo C")
            path = 'C:\\TC\\BIN\\DB.EXE'
            os.startfile(path)

        elif 'whatsapp' in query:
            try:
                print("Give the name of the receiver")
                speak("Give the name of the receiver")
                di = {
                    "Suraj": "+910000000",
                    "Vikram": "+918191015371",
                    "Ajgar": "+910000000000"
                }
                number = di[takeCommand()]

                print("What message do you want to send?")
                speak("What message do you want to send?")
                whatmsg = takeCommand()

                print("Time in hour.")
                speak("Time in hour.")
                hour = int(takeCommand())
                print(hour)

                print("Time in minute.")
                speak("Time in minute.")
                minu = int(takeCommand())
                print(minu)

                kit.sendwhatmsg(number, whatmsg, hour, minu)
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this... Try again..")

        elif 'close music' in query:
            os.system('taskkill /f /im vlc.exe')

        elif 'close file' in query:
            os.system('taskkill /f /im explorer.exe')

        elif 'close chrome' in query:
            os.system('taskkill /f /im chrome.exe')

        elif 'turn off pc' in query:
            speak("When should the PC turn off? Give time in seconds.")
            shut = int(takeCommand())
            shuts = str(shut)
            os.system('shutdown -s -t ' + shuts)
            print(f"PC will turn off in {shuts} seconds.")
            speak(f"PC will turn off in {shuts} seconds.")

        elif 'cancel' in query:
            cont = "shutdown /a"
            os.system(cont)
            print("Ok sir, Don't worry. I will not shut down your system.")
            speak("Ok sir, Don't worry. I will not shut down your system.")

        elif 'hello' in query:
            print("Hello sir, What can I do for you..")
            speak("Hello sir, What can I do for you..")

        elif 'weather' in query:
            try:
                api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=248932e95581539a55245ccabc4b8e65&q='
                unit = '&units=metric'
                speak("Tell me the city name.")
                city = takeCommand()
                url = api_address + city + unit
                json_data = requests.get(url)
                data = json_data.json()

                temp = data['main']['temp']
                temp = str(temp)

                hum = data['main']['humidity']
                hum = str(hum)

                wind = data['wind']['speed']
                wind = wind * 2
                wind = str(wind)

                vis = data['visibility']
                vis = vis / 100
                vis = str(vis)

                discript = data['weather'][0]['main']
                discript = str(discript)

                print("Temperature is ", temp, " degree Celsius..")
                speak("Temperature is " + temp + " degree Celsius..")

                print("Humidity is ", hum, " percent..")
                speak("Humidity is " + hum + " percent..")

                print("Wind speed is ", wind, " miles per hour..")
                speak("Wind speed is " + wind + " miles per hour..")

                print("Description of visibility is ", discript)
                speak("Description of visibility is " + discript)

                print("Visibility is ", vis, " meters..")
                speak("Visibility is " + vis + " meters..")
            except Exception as e:
                print("Sorry Sir. I am not able to give you the weather report. Try again..")
                speak("Sorry Sir. I am not able to give you the weather report. Try again..")
