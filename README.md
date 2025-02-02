# TransvoX 🚀🎙️ - Real-Time Speech Translator

## 🎙️ About TransvoX 🚀🎙️
**TransvoX 🚀🎙️** is a real-time speech translation and text-to-speech application built using **Python, Streamlit, Google Text-to-Speech (gTTS), and Speech Recognition**. It enables users to speak in one language and hear the translated output in another, making multilingual communication seamless and effective.

---
## ✨ Features
✅ **Real-time Speech Recognition** – Converts spoken words into text using `speech_recognition`.
✅ **Multi-Language Translation** – Supports various languages using `googletrans`.
✅ **Text-to-Speech (TTS) Conversion** – Uses `gTTS` to convert translated text into speech.
✅ **Interactive UI** – Built with **Streamlit** for a simple and user-friendly interface.
✅ **Supports Multiple Languages** – Translate and speak in different languages.

---
## 📌 Installation Guide

### 🔹 Prerequisites
Ensure you have **Python 3.8+** installed. You can check your version using:
```bash
python --version
```

### 🔹 Install Required Dependencies
Run the following command to install the required Python libraries:
```bash
pip install streamlit speechrecognition gtts pygame googletrans==4.0.0-rc1
```

### 🔹 Run the Application
To start the application, execute the following command:
```bash
streamlit run app.py
```

---
## 🛠️ How It Works
1. **User selects the source and target language** from the dropdown menus.
2. **Click "Start"** – The app listens for spoken input.
3. **Speech is recognized and converted to text.**
4. **Text is translated** into the selected target language.
5. **Translated text is converted to speech** using Google TTS.
6. **Click "Stop"** to end the process.

---
## 📜 Code Overview

### 🔹 Import Necessary Libraries
```python
import os
import pygame
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from googletrans import LANGUAGES, Translator
```

### 🔹 Initialize Translator and Audio Engine
```python
translator = Translator()
pygame.mixer.init()
```

### 🔹 Convert Language Name to Code
```python
language_mapping = {name: code for code, name in LANGUAGES.items()}
def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)
```

### 🔹 Speech-to-Text Function
```python
def speech_to_text(from_language):
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio = rec.listen(source, phrase_time_limit=10)
    return rec.recognize_google(audio, language=from_language)
```

### 🔹 Translate Text
```python
def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src=from_language, dest=to_language)
```

### 🔹 Convert Text to Speech
```python
def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang=to_language, slow=False)
    myobj.save("cache_file.mp3")
    pygame.mixer.Sound("cache_file.mp3").play()
    os.remove("cache_file.mp3")
```

### 🔹 UI with Streamlit
```python
st.title("LinguaSpeak - Real-Time Speech Translator")
from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

if st.button("Start"):
    spoken_text = speech_to_text(from_language)
    translated_text = translator_function(spoken_text, from_language, to_language)
    text_to_voice(translated_text.text, to_language)
    st.write(f"Translated Text: {translated_text.text}")

---
## 📬 Contact
For any queries or suggestions, feel free to reach out:
📧 Email: sujanshetty003@gmail.com
📌 GitHub: https://github.com/SujanShetty003
📌 LinkedIn: https://www.linkedin.com/in/sujan-r-5a629324a/

---
🌟 If you like this project, give it a ⭐ on GitHub!

