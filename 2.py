import speech_recognition as sr
import random
import gtts as GTTS
import pygame as pg


pg.init()
pg.mixer.init()


def pl(gr):
    tts = GTTS.gTTS(text=gr, lang='fr')
    tts.save('speech.mp3')
    pg.mixer.music.load('speech.mp3')
    return pg.mixer.music.play()


def recogn(r):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    transcript_str = r.recognize_google(audio, language='fr-FR', show_all=False)
    return transcript_str



def greeting(rec_str):
    greeting_inp = ['Bonjour', 'Salut', 'Bonsoir']
    greeting_req = ['Bonjour', 'Salut', 'Bonsoir']
    for i in rec_str.split():
        if i in greeting_inp:
            return random.choice(greeting_req)

def main():
    try:
        r = sr.Recognizer()
        while True:
            rec_str = recogn(r)
            if 'bonjour' in rec_str or 'Bonjour' in rec_str:
                print(rec_str)
                gr = greeting(rec_str)
                print(gr)
                pl(gr)

                rec1_str = recogn(r)
                print(rec1_str)
                if 'tu me comprends' in rec1_str:
                    w = 'oui, qu\'est-ce que tu veux?'
                    print(w)
                    pl(w)

                if 'rien' in rec1_str:
                    w = "alors, je ne veux pas t'ecouter"
                    print(w)
                    pl(w)
            if 'stop' in rec_str:
                w = 'stop'
                break
    except NameError:
        print('Pourqoi tu ne veux pas parler avec moi?')
    except sr.UnknownValueError:
        print('Je ne te comprends pas')

main()