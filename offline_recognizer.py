import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=3.0)
print(r.recognize_sphinx(audio))