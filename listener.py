import pyperclip
import datetime
import time
import os
from threading import Thread


words = []
lastword =""
curword =""
A_Z = 'abcdefghijklmnopqrstuvwxyz'


def submit():
    os.system('play ok.wav')

def backup():
    while True:
        time.sleep(60)
        with open('[history]-[%s].txt'%datetime.datetime.now().date(),'a+') as f:
            f.write('\n'.join(words))
            print("!!!!!!!!!!!!!!!")
    

t = Thread(target=backup)
t.start()
def isWord(tmp):
    tmp = tmp.strip()
    tmp = tmp.lower()
    res = tmp.split(' ')
    if len(res) == 1:
        for c in res[0]:
            if c not in A_Z:
                return False
        return  res
    return False

while True:
    time.sleep(0.5)
    tmp = pyperclip.paste()
    curword = isWord(tmp)
    if curword == lastword or not curword:
        continue
    lastword = curword
    submit()
    words.append('|%s|%s'%(curword[0],datetime.datetime.now()))
    print(words)


