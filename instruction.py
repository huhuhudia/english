import os
from pocketsphinx import LiveSpeech
def recongitionInstruction():
    for phrase in LiveSpeech(): 
        phrase = str(phrase)
        print(phrase)
        if phrase == 'open terminal':
            os.system('gnome-terminal')
        if phrase == 'google':
            print('open google !!')
            os.system('google-chrome-stable')

recongitionInstruction()