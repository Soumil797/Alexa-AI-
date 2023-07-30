import os
import speech_recognition as sr


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

while True:
    wake_up = takeCommand()

    if ('wake up') in wake_up:
        os.startfile("")