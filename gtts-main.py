from gtts import gTTS as tts
from playsound import playsound
import os

langCode = input('Language code: ')
text = input('Text: ')
fname = input('File name: ') + '.mp3'
kept = input('Kept this file? [Y/n]: ').lower()[0]

isKept = True if kept == 'y' else False

audio = tts(text, lang_check = False, lang = langCode)
audio.save(fname)

print('Playing audio file...')
playsound(fname)

if not isKept:
    os.remove(fname)