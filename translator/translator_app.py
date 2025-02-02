import os
import time

import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

isTranslateOn = False

translator = Translator() # Initialize the translator module.
pygame.mixer.init()  # Initialize the mixer module.

# Create a mapping between language names and language codes,revrse the dictionary
language_mapping = {name: code for code, name in LANGUAGES.items()}
# language_mapping = {
#     'french': 'fr',
#     'english': 'en',
#     'hindi': 'hi'
# }

#  Understanding .get() Method in Python
# The .get() method in Python retrieves a value from a dictionary for a given key.
# It takes two parameters:
# dictionary.get(key, default_value)
# If key exists in the dictionary → returns the corresponding value.
# If key does NOT exist → returns the default_value instead of raising an error.

# If language_name exists in language_mapping → it returns the corresponding language code.
# If language_name does NOT exist in language_mapping → it returns the same input (language_name) instead of throwing an error.
# Ex language_mapping.get("french", "french"),"french" exists in language_mapping, so it returns "fr".
# language_mapping.get("xyz", "xyz")
# "xyz" does not exist in language_mapping.
# Instead of causing an error, .get() returns the default value, which is "xyz"

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

# Uses Google Translate to convert spoken_text from from_language to to_language.
# Ex translator_function("Hello", "en", "fr")  # Output: "Bonjour"

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

def text_to_voice(text_data, to_language):
    # Uses Google Text-to-Speech (gTTS) to convert the text into speech audio.
    # text=text_data → Uses the input text.
    # lang=to_language → Specifies the language code (e.g., "en" for English, "fr" for French).
    myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False) # Slow =false means normal speed,true means slowerspeed    Ex:    myobj = gTTS(text="Hello, how are you?", lang="en", slow=False)
    myobj.save("cache_file.mp3")   #  Saves the generated speech as an MP3 file named "cache_file.mp3" ,, 📁 cache_file.mp3  (contains "Hello, how are you?" in English speech)
    audio = pygame.mixer.Sound("cache_file.mp3")  # Uses Pygame’s mixer module to load the audio file. The Sound object allows us to play the audio.
    audio.play()  # Plays the generated audio file. You will hear the spoken text. Ex  You will hear "Hello, how are you?" spoken aloud.
    os.remove("cache_file.mp3") #  Removes "cache_file.mp3" after playing. This prevents unnecessary files from accumulating.

# Step 1: gTTS converts "Bonjour, comment ça va ?" into a French audio file.
# Step 2: Saves it as "cache_file.mp3".
# Step 3: Pygame loads the audio file.
# Step 4: Plays the spoken text.
# Step 5: Deletes "cache_file.mp3" after playing.

def main_process(output_placeholder, from_language, to_language):
    
    global isTranslateOn  # To Access the Global Variable
    
    while isTranslateOn:  # When isTranslateOn is True, the loop will keep running until isTranslateOn is set to False.

        rec = sr.Recognizer()  # Initialize Speech Recognizer, Creates an instance of Recognizer() from speech_recognition to capture and process speech.
        with sr.Microphone() as source:  # Uses the microphone to capture live audio input.
            output_placeholder.text("Listening...")  # Displays "Listening..." in the Streamlit UI to inform the user.
            rec.pause_threshold = 1  # Sets a 1-second pause threshold for detecting the end of speech. If the user stops speaking for 1 second, the program stops recording.
            audio = rec.listen(source, phrase_time_limit=10)   # Listens to the microphone and records audio for a maximum of 10 seconds.
        
        try:
            # Convert Speech to Text
            output_placeholder.text("Processing...")
            spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))   # User Speaks (in English) "Hello, how are you?",  Recognized Text  is a  spoken_text = "Hello, how are you?"
            # Translate the Text
            output_placeholder.text("Translating...")
            translated_text = translator_function(spoken_text, from_language, to_language)   # Calls the translator function to translate the spoken text.  Ex  translated_text = translator_function("Hello, how are you?", "en", "es")
            # translated_text = "Hola, ¿cómo estás?"


            # Convert Translated Text to Speech
            text_to_voice(translated_text.text, to_language)  #   Calls text_to_voice() to convert the translated text into speech, Ex  text_to_voice("Hola, ¿cómo estás?", "es")
    
        except Exception as e:
            print(e)      # Handle errors (e.g., no speech detected)

# UI layout
st.title("Language Translator")

# Dropdowns for selecting languages
from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Button to trigger translation
start_button = st.button("Start")
stop_button = st.button("Stop")

# Check if "Start" button is clicked
if start_button:
    if not isTranslateOn:  # To check translation is already running 
        isTranslateOn = True
        output_placeholder = st.empty()
        # Creates an empty placeholder in the Streamlit UI.
        # This placeholder will be updated dynamically (e.g., showing "Listening...", "Processing...", "Translating...").
        # Instead of adding new lines, the placeholder overwrites the previous text.
        main_process(output_placeholder, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    isTranslateOn = False






