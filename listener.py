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

HEAD ='| word | time | url |\n| ------------ | ------------ | ------------ |\n'
def submitWord():
    print('submit word')
    os.system('play submit-word.wav')
def submitSentence():
    print('submit sentence')
    os.system('play submit-sentence.mp3')
EXIST = False
def backup():
    global EXIST
    while True:
        print('++==++==++==++==++==')
        time.sleep(30)
        with open('/home/yyy/Desktop/english/history/[history]-[%s].md'%datetime.datetime.now().date(),'a+') as f:
            if len(words) != 0 and EXIST == False:
                f.write( HEAD +'\n'.join(words))
                EXIST = True
            elif len(words) !=0 and EXIST == True:
                f.write('\n' +'\n'.join(words))
            words.clear()
            print("!!!!!!!!!!!!!!!")
        with open('/home/yyy/Desktop/english/sentence/[sentence]-[%s].md'%datetime.datetime.now().date(),'a+') as f:
            if len(sentences) != 0:
                f.write( '\n'+ '\n'.join(sentences))
            sentences.clear()
            print("==============")
    

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


    
def isSentenceAndTranslation(tmp):
    
    res = tmp.split('\n')
    print(res)
    first_line = ""
    last_line = ""
    for line in res:
        if line.strip():
            first_line = line
            break
    for line in res[::-1]:
        if line.strip():
            last_line = line
            break

    first_line_split = first_line.split(' ')
    flag1 = False
    flag2 = False
    print("first line :\n\n",first_line_split)
    print('last_lineL \n\n\'',last_line)
    for word in first_line_split:
        if isWord(word):
            flag1 = True
            break   
    for word in last_line:
        if '\u4e00' <= word <= '\u9fa5':
            flag2 = True
            break
    print(flag1 and flag2)
    return flag1 and flag2


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
        if phrase == 'open WIFI':
            os.system('nmcli device wifi hotspot con-name my-hotspot ssid my-hotspot band bg password xwt123456')
        if phrase == 'open file server':
            os.system('/home/yyy/YunDisk/chfs  --file=/home/yyy/YunDisk/config')
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
        words.append('|%s|%s|https://fanyi.baidu.com/#en/zh/%s|'%(curword,datetime.datetime.now(),curword))
        # print(words)  
        continue  


    if isSentenceAndTranslation(tmp):
        if lastsentence == tmp:
            continue
        lastsentence = tmp
        sentences.append('```\n' + tmp +'\n```')
        submitSentence()
        
        

