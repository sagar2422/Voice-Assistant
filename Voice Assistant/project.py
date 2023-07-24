import subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os , sys
import webbrowser
import wolframalpha
import pyjokes
import pyautogui
from tkinter import *
import pywhatkit
import psutil

class screenshot:
    def takeSS(self):
        img_captured = pyautogui.screenshot()
        a = os.getcwd()
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")
        os.chdir(a + '\Screenshots')
        ImageName = 'screenshot-' + str(datetime.datetime.now()).replace(':', '-') + '.png'
        img_captured.save(ImageName)
        os.startfile(ImageName)
        os.chdir(a)


class note:
    def Note(self, data):
        date = datetime.datetime.now()
        filename = str(date).replace(':', '-') + '-note.txt'
        a = os.getcwd()
        if not os.path.exists('Notes'):
            os.mkdir('Notes')
        os.chdir(a + r'\Notes')
        with open(filename, 'w+') as f:
            f.write(data)
        subprocess.Popen(['notepad.exe', filename])
        os.chdir(a)


engine = pyttsx3.init("sapi5")
female = engine.getProperty('voices')
engine.setProperty('voice', female[1].id)
engine.setProperty("rate", 140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning")
        speak("Good morning")
    elif hour > 12 and hour < 16:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    print("I am your personal voice assistant Natasha")
    speak("I am your personal voice assistant Natasha")
    print("How may i help you")
    speak("How may i help you")


def take_Command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 10000
        audio = r.listen(source)
    try:
        print("Recognizing....")
        querry = r.recognize_google(audio, language='en-in')
        print("user command: " + querry)
    except:

        print("Can you say that again??")
        return "None"
    return querry





# def gui():
#         root = Tk()
#
#         root.title('Natasha')
#         root.geometry('520x320')
#         compText = StringVar()
#         userText = StringVar()
#         userText.set('Your Virtual Assistant')
#         userFrame = LabelFrame(root, text='Natasha', font=('Railways', 24,
#                                                            'bold'))
#         userFrame.pack(fill='both', expand='yes')
#         top = Message(userFrame, textvariable=userText, bg='black', fg='white')
#         top.config(font=("Century Gothic", 15, 'bold'))
#         top.pack(side='top', fill='both', expand='yes')
#         btn = Button(root, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white',command=voice()).pack(fill='x', expand='no')
#         root.mainloop()


def voice():


        wishme()
        # Widget()
        while True:

            command = take_Command().lower()

            if 'natasha' in command:
                command = command.replace("natasha", "")

            if "wikipedia" in command  or "search on wikipedia" in command:
                print("Searching on Wikipedia....")
                speak("Searching on Wikipedia....")
                if "wikipedia" in command:
                        command = command.replace("wikipedia", "")
                elif "search on wikipedia" in command:
                        command = command.replace("search on wikipedia", "")
                result = wikipedia.summary(command, sentences=1)
                print(f"According to wikipedia{result}")
                speak(f"According to wikipedia{result}")
                print(result)

            elif "who are you" in command or "what is your name" in command:
                print("I am Natasha , Created by Bhushan ,Omkar , Sagar , Chetan")
                speak("I am Natasha , Created by Bhushan ,Omkar , Sagar , Chetan")

            elif 'how are you' in command:
                print("I am fine, Thank you")
                print("How are you, Sir")
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif "hi" in command or "hello" in command :
                print("how may i help you")
                speak("how may i help you")

            elif 'fine' in command or "good" in command:
                print("It's good to know that your fine")
                speak("It's good to know that your fine")

            elif "battery percentage" in command:
                battery = psutil.sensors_battery()
                percent = battery.percent
                print(f"Battery percentage is {percent} percent")
                speak(f"Battery percentage is {percent} percent")

            elif "tell time" in command or "Whats time right now" in command or "time" in command:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strtime)
                speak(strtime)


            elif "open vs code" in command or  " open Visual studio Code" in command:
                print("opening vs code")
                speak("opening vs code")

                path = "C:\\Users\\bhush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            elif "open netbeans" in command:
                print("opening Apache Netbeans")
                speak("opening Apache Netbeans")
                path = "C:\\Program Files\\NetBeans-12.5\\netbeans\\bin\\netbeans64.exe"
                os.startfile(path)

            elif "open microsoft word" in command or "open word" in command:
                print("opening word")
                speak("opening word")
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(path)

            elif "open microsoft excel" in command or "open excel" in command:
                print("opening excel")
                speak("opening excel")
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(path)

            elif "open microsoft powerpoint" in command or "open powerpoint" in command:
                print("opening powerpoint")
                speak("opening powerpoint")
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(path)

            # elif ("open youtube") in command:
            #     print("opening youtube")
            #     speak("opening youtube")
            #
            #     webbrowser.open("https://www.youtube.com/?gl=IN")


            elif 'open google' in command:
                print("opening google")
                speak("opening google")
                webbrowser.open("https://www.google.co.in/")

            elif "calculate" in command or "what is" in command or "who" in command:
                app_id = "JRVVX9-8W47KGJHX6"
                client = wolframalpha.Client(app_id)
                res = client.query(command)
                answer = next(res.results).text
                print(answer)
                speak(answer)

            elif "tell me a joke" in command or "i want to hear some jokes"  in command:
                # print(pyjokes.get_joke(language="en", category="all"))
                speak(pyjokes.get_joke(language="en", category="all"))

            elif "one more joke" in command or "another joke" in command:
                # print(pyjokes.get_joke(language="en", category="all"))
                speak(pyjokes.get_joke(language="en", category="all"))

            elif "take screenshot" in command or "take a screenshot" in command or "screenshot" in command:
                print("Taking screenshot")
                speak("Taking screenshot")
                SS = screenshot()
                SS.takeSS()
                print("Captured screenshot is saved in Screenshots folder.")
                speak('Captured screenshot is saved in Screenshots folder.')
                del SS

            elif "exit" in command or "shut down" in command or "shutdown" in command or "close" in command:
                print("Shutting down")
                speak("shutting down")
                print("Thank you!!!!")
                speak("Thank you")
                sys.exit()


            elif "search on youtube for " in command:
                command = command.replace("search on youtube for","")
                print("searching on youtube for "+command)
                pywhatkit.playonyt(command)
            elif "search for" in command or "search on google" in command or "search" in command:
                if "search for" in command:
                    command = command.replace("search for", "")
                elif "search on google" in command:
                    command = command.replace("search on google", "")
                elif "search" in command:
                    command = command.replace("search", "")
                speak("Searching for "+command)
                print(command)
                pywhatkit.search(command)


            elif "take note" in command or "make note" in command or "take a note" in command or "note" in command:
                speak("What would you like to write down?")
                data = take_Command()
                n = note()
                n.Note(data)
                speak("I have a made a note of that.")

voice()