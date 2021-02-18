import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_id = 'com.apple.speech.synthesis.voice.samantha'
engine.setProperty('voice', voice_id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
    except:
        talk('Sorry. I did not understand. Please repeat')
    return command

def runAlexa():
    command = takeCommand()
    wiki_questions = ['who is','what is','search','wikipedia']
    if 'play' in command:
        command = command.replace('play','')
        talk('playing' + command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().time().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is' in command:
        command = command.replace('what is','')
        info = wikipedia.summary(command, 2)
        talk('I found the following information about' + command + 'on the internet' + info)
    elif 'who is' in command:
        command = command.replace('who is', '')
        info = wikipedia.summary(command, 2)
        talk('I found the following information about' + command + 'on the internet' + info)
    elif 'joke' in command:
        talk(pyjokes.get_joke('en'))
    else:
        talk("I did not understand. Please repeat")

runAlexa()


# for voice in voices:
#     # to get the info. about various voices in our PC
#     print("Voice:")
#     print("ID: %s" % voice.id)
#     print("Name: %s" % voice.name)
#     print("Age: %s" % voice.age)
#     print("Gender: %s" % voice.gender)
#     print("Languages Known: %s" % voice.languages)

