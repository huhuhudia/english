def isEnglish(line):
    for c in line[:20]:
        if c in "abcdefghijklmnopqrstuvwxyz":
            return True
    return False

stk = []

with open('sentence.txt') as f:
    res = ""
    
    for line in f.readlines():
        line = line.strip()
        if line:
    
            if isEnglish(line):
                stk.append('```')
                stk.append( line)
            else:
                stk.append( line)
                stk.append( '```')
                
    res = '\n'.join(stk)
    with open('setence.md','w+') as f:
        f.write(res)


with open('word.txt') as f:
    res = '| index | words | url |\n| ------------ | ------------ | ------------ |'
    count = 0
    for word in f.readlines():
        if not word.strip():
            continue
        count+=1
        word = word.strip()
        link = "https://fanyi.baidu.com/#en/zh/%s"%word
        line = '\n|%d|%s|%s|'%(count,word,link)
        res += line
        print(res)
    with open('word.md','w+') as f:
        f.write(res)

import os 
os.system('git add .')
os.system('git commit -m "md update"')
os.system('git push ')

