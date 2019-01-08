import pyperclip
import datetime
import time
import os
from threading import Thread
from pocketsphinx import LiveSpeech
from multiprocessing import Process


words = []
sentences =  []
lastword =""
curword =""
cursentence = ""
lastsentence = ""
A_Z = 'abcdefghijklmnopqrstuvwxyz\\'


def submitWord():
    print('submit word')
    os.system('play submit-word.wav')
def submitSentence():
    print('submit sentence')
    os.system('play submit-sentence.mp3')
def backup():
    while True:
        print('!!')
        time.sleep(60)
        with open('[history]-[%s].txt'%datetime.datetime.now().date(),'a+') as f:
            f.write( '\n'+ '\n'.join(words))
            words.clear()
            # print("!!!!!!!!!!!!!!!")
        with open('[sentence]-[%s].md'%datetime.datetime.now().date(),'a+') as f:
            f.write( '\n'+ '\n'.join(sentences))
            sentences.clear()
            # print("==============")
    

t = Process(target=backup)

t.start()
def isWord(tmp):
    tmp = tmp.strip()
    tmp = tmp.lower()
    res = tmp.split(' ')
    if len(res) == 1:
        for c in res[0]:
            if c not in A_Z:
                return False
        return  True
    return False
def recongitionInstruction():
    for phrase in LiveSpeech(): 
        print(phrase)
        if phrase == 'terminal':
            os.system('gnome-terminal')
        if phrase == 'web':
            os.system('google-chrome-stable')

    
def isSentenceAndTranslation(tmp):
    
    res = tmp.split('\n')
    # print(res)
    # print(len(res))
    if len(res) != 3:
        return False
    line1 = res[0]
    line2 = res[2]
    line1 = line1.split(' ')
    # print(line1)
    for word in line1:
        if isWord(word):
            return True
    return False

backupThread = Thread(target=backup)
backupThread.start()



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
        if phrase in ['open terminal','google']:
            os.system('play getinstruction.mp3')

instructionP = Process(target=recongitionInstruction)
instructionP.start()

while True:
    time.sleep(0.5)
    tmp = pyperclip.paste()
    
    if isWord(tmp):
        tmp = tmp.strip()
        tmp = tmp.lower()
        res = tmp.split(' ')
        curword = res[0] 
        if curword == lastword:
            continue
        lastword = curword
        submitWord()
        words.append('|%s|%s'%(curword[0],datetime.datetime.now()))
        # print(words)  
        continue  


    if isSentenceAndTranslation(tmp):
        if lastsentence == tmp:
            continue
        lastsentence = tmp
        sentences.append('```\n' + tmp +'\n```')
        submitSentence()
        
        

