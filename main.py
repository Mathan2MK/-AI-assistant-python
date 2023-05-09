import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice',voices[1].id)
def talk(text):
    bot.say(text)
    bot.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('tell..')
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            if 'moon' in command:
                command = command.replace('moon','')
                print(command)


    except:
        pass
    return command

def run_moon():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time,'')
        talk('Time' +time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d:%m:%y')
        print(date,'')
        talk('date'+date)
    elif 'search' in command:
        command = command.replace('search','')
        webbrowser.open(command)
    elif 'wikipedia'or'who'or'what' in command:
        command=command.replace('wikipedia'and'who'and'what','')
        info=wikipedia.summary(command,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else :
        print('i con not understund')
        talk("puriyala")

run_moon()


