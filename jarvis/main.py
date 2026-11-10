import speech_recognition as sr
import webbrowser
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import time
from dotenv import load_dotenv

import musicLibrary


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# ==========================================
# INITIALIZE
# ==========================================

recognizer = sr.Recognizer()

pygame.mixer.init()


# ==========================================
# TEXT TO SPEECH
# ==========================================

def speak(text):
    print("Jarvis:", text)

    try:
        tts = gTTS(text=text, lang="en")
        filename = "temp.mp3"

        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        print("Speech Error:", e)


# ==========================================
# OPENAI AI PROCESSING
# ==========================================

def aiProcess(command):

    if not OPENAI_API_KEY:
        return "OpenAI API key is missing. Please add it to your .env file."

    try:

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.responses.create(
            model="gpt-5-mini",
            instructions=(
                "You are Jarvis, a helpful virtual assistant. "
                "Give short and simple answers."
            ),
            input=command
        )

        return response.output_text

    except Exception as e:

        print("OpenAI Error:", e)

        return "Sorry, I couldn't connect to the AI service."


# ==========================================
# NEWS
# ==========================================

def get_news():

    if not NEWS_API_KEY:
        speak("News API key is missing.")
        return

    try:

        url = (
            "https://newsapi.org/v2/top-headlines"
            f"?country=in&apiKey={NEWS_API_KEY}"
        )

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            articles = data.get("articles", [])

            if not articles:
                speak("I couldn't find any news.")
                return

            speak("Here are the latest headlines.")

            for article in articles[:5]:

                title = article.get("title")

                if title:
                    speak(title)

        else:

            print("News API Error:", response.status_code)
            speak("I couldn't get the news right now.")

    except Exception as e:

        print("News Error:", e)
        speak("There was a problem getting the news.")


# ==========================================
# PROCESS COMMAND
# ==========================================

def processCommand(command):

    c = command.lower().strip()

    print("Command:", command)


    # --------------------------------------
    # GOOGLE
    # --------------------------------------

    if "open google" in c:

        speak("Opening Google.")
        webbrowser.open("https://www.google.com")


    # --------------------------------------
    # YOUTUBE
    # --------------------------------------

    elif "open youtube" in c:

        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")


    # --------------------------------------
    # FACEBOOK
    # --------------------------------------

    elif "open facebook" in c:

        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")


    # --------------------------------------
    # LINKEDIN
    # --------------------------------------

    elif "open linkedin" in c:

        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")


    # --------------------------------------
    # GITHUB
    # --------------------------------------

    elif "open github" in c:

        speak("Opening GitHub.")
        webbrowser.open("https://github.com")


    # --------------------------------------
    # PLAY MUSIC
    # --------------------------------------

    elif c.startswith("play"):

        words = c.split()

        if len(words) < 2:

            speak("Please tell me the song name.")

            return

        song = " ".join(words[1:])

        if song in musicLibrary.music:

            speak(f"Playing {song}.")

            webbrowser.open(musicLibrary.music[song])

        else:

            speak(
                f"I don't have {song} in my music library."
            )


    # --------------------------------------
    # NEWS
    # --------------------------------------

    elif "news" in c:

        get_news()


    # --------------------------------------
    # EXIT
    # --------------------------------------

    elif c in ["exit", "quit", "stop", "shutdown"]:

        speak("Goodbye.")

        raise SystemExit


    # --------------------------------------
    # AI
    # --------------------------------------

    else:

        output = aiProcess(command)

        speak(output)


# ==========================================
# LISTEN TO MICROPHONE
# ==========================================

def listen():

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.WaitTimeoutError:

        print("No speech detected.")

        return ""

    except sr.UnknownValueError:

        print("Could not understand audio.")

        return ""

    except sr.RequestError as e:

        print("Speech recognition error:", e)

        return ""

    except Exception as e:

        print("Microphone Error:", e)

        return ""


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    speak("Initializing Jarvis.")

    speak("Say Jarvis to wake me up.")

    while True:

        try:

            print("\nWaiting for wake word...")

            word = listen()

            if word == "jarvis":

                speak("Yes?")

                print("Jarvis Active...")

                command = listen()

                if command:

                    processCommand(command)

        except KeyboardInterrupt:

            print("\nJarvis stopped.")

            break

        except SystemExit:

            break

        except Exception as e:

            print("Error:", e)