import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib                  #for sending emails

engine = pyttsx3.init("sapi5")  # to take the user's voice using window's in-built api
voices = engine.getProperty("voices")
# print(voices)         #gives two voices name one male and one female

engine.setProperty("voice", voices[0].id)
# to get female voice give index as 1 and for male it is 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am jarvis sir. Please tell me how may i help you")


def sendEmail(to, content):
    # for sending the email you have to allow the less secure apps in your sending email address
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


def takeCommand():
    # it takes voice input from user and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\ABHISHEK\\Downloads"  # give the location of folder where your song is located
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif "open vscode" in query:
            codePath = '"C:\\Users\\ABHISHEK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)
        elif "email to harry" in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "abhishek523240@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry i'm not able to sent the email at the moment")
        elif "quit" in query:
            exit()
        else:
            speak("Please say something")
