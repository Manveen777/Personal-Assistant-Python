# Personal-Assistant-Python

# 🎙️ Personal Assistant Python

A simple **voice-controlled personal assistant** built in Python.
It listens to your voice, talks back, tells jokes, searches Wikipedia, opens websites, and more.

---

## ✨ Features

* 🎤 Speech recognition (listen to your voice)
* 🔊 Text-to-speech (assistant talks back)
* 🌐 Open websites (YouTube, Google, etc.)
* 📖 Wikipedia search
* 😂 Tell jokes
* 🖥️ System commands (open apps, etc.)

---

## 📦 Requirements

Make sure you have **Python 3.8+** installed.

Install dependencies with:

```bash
pip install -r requirements.txt
```

### `requirements.txt` example:

```
speechrecognition
pyttsx3
wikipedia
requests
pyjokes
pyaudio
```

---

## ▶️ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/personal-assistant-python.git
   cd personal-assistant-python
   ```

2. Run the assistant:

   ```bash
   python assistant.py
   ```

3. Speak commands like:

   * “Hello”
   * “Open YouTube”
   * “Search Wikipedia for Python”
   * “Tell me a joke”

---

## ⚠️ Notes

* **Microphone access** must be enabled on your system.
* If you have multiple microphones, edit the `device_index` in the code.
* On Windows, you may need to install **PyAudio wheel** manually if `pip install pyaudio` fails.
* This is just the demo of what is being created
* The work on assistant is still going on. 
