import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
female = engine.getProperty('voices')
engine.setProperty('voice',female[1].id)
listener = sr.Recognizer()


def get_Command():

  try:
    with sr.Microphone() as  source:
        print("listening......")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        engine.say(command)
        engine.runAndWait()

        return command

  except:
     pass

def run_Commands():
    command = get_Command()
    if "Hello" in command:
        engine.say("I am good  how are you!!")

get_Command()
run_Commands()


