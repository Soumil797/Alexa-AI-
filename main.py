import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import pyAudio
import subprocess
import pywhatkit
import pyjokes
import requests
import pyautogui
import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst
import webbrowser



print('Loading your AI personal assistant - Alexa')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')


def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"user said:{command}\n")

        except Exception as e:
            return "None"

        return command.lower()



talk("Loading your AI personal assistant Alexa")



if __name__ == '__main__':


    while True:
        talk("Tell me how can I help you now?")
        command = takeCommand().lower()
        if command == 0:
            continue

        if "good bye" in command or "ok bye" in command or "stop" in command:
            talk('your personal assistant Alexa is shutting down,Good bye')
            print('your personal assistant Alexa is shutting down,Good bye')
            break



        if 'wikipedia' in command:
            talk('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            talk("According to Wikipedia")
            print(results)
            talk(results)
            
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'information about' in command:
            info = command.replace('information about', '')
            talk('i got this from google ' + info)
            print('I got the from google' + info)
            pywhatkit.search(info)

        elif 'join zoom' in command:
            talk("get Ready for joining the zoom call...")
            import time
            from datetime import datetime
            from pynput.keyboard import Controller, Key
            from data import lst
            import webbrowser

            keyboard = Controller()

            isStarted = False

            for i in lst:
                while True:
                    if isStarted == False:
                        if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(
                                i[1].split(':')[1]):
                            webbrowser.open(i[0])
                            isStarted = True
                    elif isStarted == True:
                        if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(
                                i[2].split(':')[1]):
                            keyboard.press('w')
                            time.sleep(1)
                            keyboard.press(Key.enter)
                            isStarted = False
                            break

        elif 'video' in command:
            video = command.replace('video', '')
            talk('playing ' + video)
            pywhatkit.playonyt(video)

        elif 'open youtube' in command or "open video online" in command:
            webbrowser.open("www.youtube.com")
            talk("opening youtube")

        elif 'open github' in command:
            webbrowser.open("https://www.github.com")
            talk("opening github")

        elif 'open facebook' in command:
            webbrowser.open("https://www.facebook.com")
            talk("opening facebook")

        elif 'open instagram' in command:
            webbrowser.open("https://www.instagram.com")
            talk("opening instagram")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            talk("opening google")

        elif 'open yahoo' in command:
            webbrowser.open("https://www.yahoo.com")
            talk("opening yahoo")

        elif 'open gmail' in command:
            webbrowser.open("https://mail.google.com")
            talk("opening google mail")

        elif 'open notepad' in command:
            subprocess.call("notepad.exe")
            talk("opening notepad")

        elif 'open command prompt' in command:
            subprocess.call("cmd.exe")
            talk("opening command prompt")

        elif 'open snapdeal' in command:
            webbrowser.open("https://www.snapdeal.com")
            talk("opening snap_deal")

        elif 'open amazon' in command or 'shop online' in command:
            webbrowser.open("https://www.amazon.com")
            talk("opening amazon")
        elif 'open flipkart' in command:
            webbrowser.open("https://www.flipkart.com")
            talk("opening flipkart")
        elif 'open ebay' in command:
            webbrowser.open("https://www.ebay.com")
            talk("opening ebay")

        elif "shutdown" in command:
            talk("shutting down")
            os.system('shutdown -s')
        elif 'make you' in command or 'created you' in command or 'develop you' in command:
            ans_m = " For your information Soumil Saha Created me ! I give Lot of Thanks to Him "
            print(ans_m)
            talk(ans_m)
        elif "who are you" in command or "about you" in command or "your details" in command:
            about = "I am Alexa, an A I based computer program . ok Lets Start "
            print(about)
            talk(about)
        elif "hello" in command or "hello Alexa" in command:
            hel = "Hello Soumil Sir ! How May i Help you.."
            print(hel)
            talk(hel)
        elif "open dictionary" in command:
            webbrowser.open('https://www.dictionary.com')
            talk('Opening dictionary')

        elif " open accuweather" in command:
            webbrowser.open('https://www.accuweather.com')
            talk('here you go your weather report')

        elif "whatsapp" in command:
            webbrowser.open('https://web.whatsapp.com')
            talk('opening whatsapp')

        elif "open calculator" in command:
            webbrowser.open('https://www.calculator.com')
            talk('here you can calculate your problems')

        elif "Scan a QR Code" in command:
            webbrowser.open('https://qrcodescan.in/')
            talk('Here you go, atlast i found and application for you!')

        elif "screenshot" in command:
            image = pyautogui.screenshot()
            image.save("D:\\Soumil\\Online Classes\\image.png")
            talk('I have taken the screenshot sir. You will find it in D drive, Soumil, in Online Classes folder. ')

        elif "your name" in command or "sweet name" in command:
            na_me = "Thanks for Asking my name my self ! Dot"
            print(na_me)
            talk(na_me)
        elif "you feeling" in command:
            print("feeling Very sweet after meeting with you")
            talk("feeling Very sweet after meeting with you")
        elif command == 'none':
            continue

        elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            talk("youtube is open now")
            time.sleep(5)

        elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            talk("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in command:
            webbrowser.open_new_tab("gmail.com")
            talk("Google Mail open now")
            time.sleep(5)

        elif "weather" in command:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            talk("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"] != "404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                talk(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                talk(" City Not Found ")

        elif 'who are you' in command or 'what can you do' in command:
            talk('I am Alexa version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "open stackoverflow" in command:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            talk("Here is stackoverflow")

        elif 'news' in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            talk('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
            time.sleep(5)

        elif " you need a break Alexa" in command:
            talk('Ok sir')
            break



time.sleep(3)
