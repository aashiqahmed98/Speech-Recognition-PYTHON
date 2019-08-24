import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say something:")
    audio=r.listen(source)
    print("Got you...,wait")
try:
    WhatUSpoke=r.recognize_google(audio,language="ta-IN")
    print("In tamil:",WhatUSpoke)
except:
    pass
