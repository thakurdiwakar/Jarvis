import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import dirs 
from selenium import webdriver #chrome external window
import time
import requests  #for weather 
import subprocess   #all internal exe file
from datetime import date
import calendar


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
cdriver='C:\\Users\\diwakar singh\\Downloads\\chromedriver'


sst=dirs.mains2
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!, Sir")
        speak("Good Morning!, Sir")

    elif hour>=12 and hour<18:
        print("Good Afternoon!, Sir.. ")   
        speak("Good Afternoon!, Sir.. ")   

    else:
        print("Good Evening!, Sir")  
        speak("Good Evening!, Sir")  

    print("I am Jarvis, The AI Assistant of Diwakar ... How can i help you...!  ") 
    speak("I am  Jarvis, The AI Assistant of, Diwakar... How can i help you...!  ") 
    
    
     
    # print(speak)      

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
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
    
    cmd=1
    while cmd:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif (('quit' in query) or ('exit' in query) or('keep quiet' in query)or('good night'in query)):
            if'good night'in query:
                hour = int(datetime.datetime.now().hour)
                if ((hour>=21 and hour<24)or(hour>=0 and hour<=2)):
                    speak("Ok sir, Good Night.. I am always with you sir, bye, Take care..")
                    cmd=0
                else:
                    speak("No sir.. Dont make me a fool... ")
            else:
                speak("Ok sir.. i hope, i did well, bye sir, Take care..")
                cmd=0
        elif (('good morning' in query)or('good afternoon' in query)or('good evening'in query)):
            
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")

            elif hour>=12 and hour<18:
               print("Good Afternoon! sir...")
               speak("Good Afternoon! sir...")
            elif hour>=18 and hour<24:
                print("Good evening sir..")      
                speak("Good evening sir..")      
        elif 'play' in query:
            
            query = query.replace("play","")
            query=query.replace("search","")
            kit.playonyt(query)
            print(f"playing, {query}")
            speak(f"playing, {query}")
            

        elif 'open google' in query:
            print("opening google....")
            speak("opening google....")
            url="google.com"
            #chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.get(chrome_path).open(url)
            
            
        elif 'google' in query:
            query = query.replace("in","")
            query = query.replace("on","")
            query = query.replace("google","")
            query=query.replace("search","")
            tab = "http://google.com/?#q="
            webbrowser.open(tab+query)
            speak("Result on your screen")

        elif 'open gmail'in query:
            speak("ok sir, opening gmail")
            webbrowser.open("www.gmail.com")
            speak("Gmail on your screen, Sir...")
            
        elif 'open facebook'  in query :
            print("opening facebook....")
            speak("opening facebook....")
            url='www.facebook.com'
            speak("Facebook on your screen, Sir...")
            webbrowser.get(chrome_path).open(url)
        
        elif 'open whatsapp' in query:
            # webbrowser.open("www.whatsappweb.com") 
            print("opening whatsapp....")
            speak("opening whatsapp....")
            url='web.whatsapp.com'
            speak("Whatsapp on your screen, Sir...")
            webbrowser.get(chrome_path).open(url) 
        elif'show my last'in query:
            file = open("pywhatkit_dbs.txt","r",encoding='utf-8')
            content = file.read()
            file.close()
            if content == "--------------------":
                content = None
            print(content)
            speak(content)
            
            
             

        elif 'open control' in query:
            print("opening Control panel....")
            speak("opening Control panel....")
            subprocess.call('control.exe')
            speak("Control Panel on your screen, Sir...")
        elif 'open file' in query:
            speak("Opening File Explorer")
            subprocess.call('explorer.exe')
            speak("File explorer on your screen, Sir...")

        elif (('music' in query)or('gana'in query)):
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print("Ok Sir, Playing music....")
            speak("ok Sir, Playing music....")
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[5]))
        elif "time" in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"The Time is {strTime}")
            speak(f" the time is {strTime}")

        elif (('open visual studio' in query) or ('open vs code'in query)):
            codePath ="C:\\Users\\SBK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif('about' in query):
            print('Hello sir, I am Lucy, Developed By Diwakar which is Guided by, Mr. Ayaz Sir')
            speak('Hello sir, I am Lucy, Developed By, Diwakar i am Part of mini project. which is Guided by, Mr. Ayaz Sir')

        elif 'date'in query:
            today=datetime.datetime.now()
            today1=today.strftime("%d, %B, ")
            rr=str(today.year)
            today1=today1+rr
            print("Today date is.")
            print(today1)
            speak("today date is.")
            
            speak(today1)
            

        elif'today'in query:
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")               
            elif hour>=12 and hour<18:
               print("Good Afternoon! sir...")
               speak("Good Afternoon! sir...")
            elif hour>=18 and hour<24:
                print("Good evening sir..")                
                speak("Good evening sir..")
            today=datetime.datetime.now()
            today1=today.strftime("%d, %B, ")
            rr=str(today.year)
            today1=today1+rr
            print("today date is...",today1)
            speak("today date is..."+today1)             
            date = date.today()
            st=calendar.day_name[date.weekday()]
            print("today is, ",st)
            speak("today is, "+st)
        elif'day'in query:
            date = date.today()
            st=calendar.day_name[date.weekday()]
            speak("today is, "+st)
            print("today is, ",st)                  
        elif 'send email' in query:
            try:
                speak("Give the Name of Reciever.")
                dic={
 
                     "Suraj"   : "s@xyz.com",
                     "Bhanu" : "bh@xyz.com",
                     "Diwakar" : "ds6228353@gmail.com",
                     "Ayush"  : "ay@xyz.com",
                     "Rahul" : "ka@xyz.com",
                     

                     }
                
                so=to=takeCommand()
                to=dic[to]
                speak("What should I say?")
                content = takeCommand()               
                sendEmail(to, content)
                speak(f"Email has been sent! to ,{so}, Thankyou....")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif (('who are you' in query) or ('your name' in query)):
            print('I am AI Based Lucy,. i am assistant of Diwakar...  ')
            speak('I am AI Based Lucy,. i am assistant of,  Diwakar....  ')

        elif 'favourite song' in query:
            speak("my favroit song is, Megenta riddim.. Do you want to play")
            query=takeCommand().lower()
            if (('yes' in query) or('yah' in query)):
              url='https://www.youtube.com/watch?v=op4B9sNGi0k'
              speak("Playing My Favorite song")
              webbrowser.get(chrome_path).open(url)  
            else:
                speak("ok sir, no problem")  
        elif 'open turbo c' in query:
            speak("opening Turbo C")
            path='C:\\TC\\BIN\\DB.EXE'
            os.startfile(path)
        
        elif 'whatsapp' in query:
            try: 
                print("Give the name of reciever")
                speak("Give the name of reciever")
                di={
                     "Suraj" : "+910000000",
                     "Diwakar" : "+91600000",
                   
                     "Ajgar"  :"+910000000000"
                     }
                number=di[takeCommand()]
            
                print("What message you want to send.")
                speak("What message you want to send.")
                whatmsg=takeCommand()
                print("Time in hour.")
                speak("Time in hour.")
                hour=int(takeCommand())
                print(hour)
                print("Time in minute.")
                speak("Time in minute.")
                minu=int(takeCommand())
                print(minu)
                kit.sendwhatmsg(number,whatmsg,hour,minu)
            except Exception as e :
                print(e)
                speak("Sorry Sir. I am not able to send this...     Try again..")
        
        elif 'close music' in query:
            os.system('taskkill /f /im vlc.exe')
        elif 'close file' in query:
            os.system('taskkill /f /im explorer.exe')
        elif 'close chrome' in query:
            os.system('taskkill /f /im chrome.exe')
        
        elif 'turn off pc' in query:
            speak("When pc will turning off..Give time in second..")
            shut=int(takeCommand())
            shuts=str(shut)
            os.system('shutdown -s -t '+shuts) 
            print("pc will turning off in ",shuts, " second..")
            speak("pc will turning off in "+shuts+ " second..")
        elif 'cancel'in query:
            cont = "shutdown /a"
            os.system(cont)
            print("Ok sir,Dont worry I will not shut down your system")
            speak("Ok sir,Dont worry, I will not shut down your system")
        elif 'hello' in query:
            print("Hello sir, What can i do for you..")    
            speak("hello sir, What can i do for you..") 
           
        elif 'weather' in query:
            try:  
                api_address='http://api.openweathermap.org/data/2.5/weather?appid=248932e95581539a55245ccabc4b8e65&q='
                unit='&units=metric'
                speak("Tell me city name.")
                city=takeCommand()
                url= api_address + city+unit
                json_data= requests.get(url)

                data=json_data.json()
                temp=data['main']['temp']
                temp=str(temp)
                hum=data['main']['humidity']
                hum=str(hum)
                wind=data['wind']['speed']
                wind=wind*2
                wind=str(wind)
                vis=data['visibility']
                vis=vis/100
                vis=str(vis)
                discript=data['weather'][0]['main']
                discript=str(discript)
                     
                print("tempreature is ",temp," degree celcius..")
                speak("tempreature is "+temp+" degree celcius..")
            
                print("Humidity is ",hum," percent..")
                speak("Humidity is "+hum+" percent..")
            
                print("Speed of wind is ",wind," miles per hour..")
                speak("Speed of wind is "+wind+" miles per hour..")

                print("Discription of Visibility is ",discript)
                speak("Discription of Visibility is "+discript)
            
                print(" Visibility is ",vis," metre..")
                speak(" Visibility is "+vis+" metre..")
            except Exception as e :
                print("")
                speak("Sorry Sir. I am not able to Give you Report, Try again..")                  
        elif 'university' in query:
            try:
                speak("Opening I L I login page, Sir")
                username = [dirs.std]
                password = [dirs.mains]
                url = 'https://ilizone.iul.ac.in/login/index.php'
                speak("Opening chrome...")
                driver = webdriver.Chrome(cdriver)
                driver.get(url)
                
                cd=1
                while cd:

                    speak("What can i do.. Sir")
                    query=takeCommand().lower()
                    if'account' in query:
    
                        driver.find_element_by_id('username').send_keys(username)
                        driver.find_element_by_id('password').send_keys(password)
                        speak("Username and password succesfully enterd")
                        time.sleep(1)
                        driver.find_element_by_id('loginbtn').click()
                        speak("Welcome to Integral university Portal.")
                        time.sleep(1)
                        
                        cm=1
                        while cm:
                            
                            try:
                                driver.find_element_by_xpath("//button[@aria-expanded='false']").click()
                                time.sleep(2)
                            except Exception as e :
                                print("")
                            speak("What can i do next...")
                            diff={
                                'c + + lab'  :  'CA206_B',
                                'c plus plus':  'CA203_B',
                                'accountancy':  'BM228_B',
                                'database lab': 'CA207_B',
                                'mathematics' : 'MT202_B',
                                'database'    : 'CA204_B',
                                'multimedia'  : 'CA202_B',
                                'mini project': 'CA205_B'

                             }
                            try:
                                query=takeCommand().lower()
                                query=query.replace("open ","")
                                query=query.replace("Lucy ","")
                                query=query.replace("hey ","")
                                query=query.replace("hello ","")
                                st=query
                                query=diff[query]
                                driver.find_element_by_link_text(query).click()
                                speak("ok sir, Opening "+st+" section")
                            except Exception as e :
                                if'back'in query:
                                    speak("ok sir, i am going to back")
                                    driver.back()
                                elif 'close'in query:
                                    speak("ok sir, closing window")
                                    driver.close()
                                    break
                                elif'maximize'in query:
                                    speak("ok sir, maximizing window")
                                    driver.maximize_window()
                                elif'announcements'in query:
                                    speak("Ok sir, Opening Announcements section")
                                    driver.find_element_by_xpath("//span[@class='instancename']").click()
                                elif'submit'in query:
                                    time.sleep(1)
                                    try:
                                        driver.find_element_by_link_text('Submit attendance').click()
                                        speak("ok sir,Don't worry, i will sumbit your attendance")
                                        time.sleep(1)
                                        driver.find_element_by_xpath("//input[@class='form-check-input ']").click() #<input class="form-check-input "
                                        time.sleep(1)    
                                        driver.find_element_by_xpath("//span[@data-fieldtype='submit']").click()    #<span data-fieldtype="submit"
                                        speak("Sir, Your attendance was successfully submitted...")
                                    except Exception as e :
                                        speak("Sorry sir, i can't submit your attendance right now..")
                                elif'attendance' in query:
                                    speak("ok sir, Opening Attendance section")
                                    driver.find_element_by_link_text("Attendance").click()
                                    speak("Attendance section opened successfully... ")
                                    time.sleep(2)
                                
                                elif'minimize'in query:
                                    speak("ok sir, minimizing window")
                                    driver.minimize_window()
                                else:
                                    cm=1
                        cd=0            
                    elif 'close' in query:
                        speak("Closing tab from chrome")
                        cd=0
                        driver.close()
                    elif'maximize'in query:
                        driver.maximize_window()
                        speak("Maximizing window Successfully")
                    else:
                       speak("sorry sir, your given command is not valid ")                                         
            except Exception as e :
                print("")
                speak("Sorry Sir. I am not able to Give you Report, Try again..")     

            
               
            #driver.find_element_by_id('span.multiline').click()
            
            #speak("successfully logged into your integral learning initiative account")
            

          
