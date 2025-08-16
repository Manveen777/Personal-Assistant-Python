import datetime
import speech_recognition as sr 
import pyttsx3 
import wikipedia
import webbrowser
import requests
import pyjokes
import os

def speak(text):
    """Make Jarvis speak the given text."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # choose voice [0]=male, [1]=female
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to user voice and return as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception:
        print("Sorry, I didn't catch that. Please say again...")
        return "None"
    return query.lower()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I am your personal assistant. How can I help you?")

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except:
        speak("Sorry, I could not find anything on Wikipedia.")

def get_weather(city):
    api_key = "your_openweathermap_api_key"  # <-- put your API key here
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + api_key + "&q=" + city
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            temp = round(main["temp"] - 273.15, 2)
            desc = data["weather"][0]["description"]
            weather_info = f"Temperature in {city} is {temp} degree Celsius with {desc}."
            print(weather_info)
            speak(weather_info)
        else:
            speak("City not found.")
    except:
        speak("Sorry, I couldn't get the weather right now.")

def write_note(note):
    with open("notes.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {note}\n")
    speak("Note written successfully.")

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            search_wikipedia(query)

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "open github" in query:
            webbrowser.open("https://github.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "date" in query:
            today = datetime.date.today()
            speak(f"Today's date is {today}")

        elif "weather" in query:
            speak("Tell me the city name")
            city = take_command()
            get_weather(city)

        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "note" in query:
            speak("What should I write?")
            note = take_command()
            write_note(note)

        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a nice day.")
            break

        elif query == "none":
            continue

        else:
            speak("I did not understand, please say that again.")

