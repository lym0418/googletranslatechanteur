from urllib import request

import re
import urllib.parse

def sing(path):
    lyric={}
    lyric=lyrics(path)
    print (lyric)
    print  (lyric.keys())
    for i in lyric.keys():
        a=(str)(i)
        a=a[1:3]+a[4:6]+a[7:9]
        translate((str)(lyric[i]),a)
    print("Downloading is finished")


def lyrics(path):
    lyric={}
    file=open(path,'r')
    line=file.readlines()
    for i in range (0,len(line)):
          lyric[line[i][0:10]]=line[i][10:-1]
    file.close()
    print("file closed")
    return lyric


def translate(word,name):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    wordnew=request.quote(word)
    url="http://translate.google.com/translate_tts?tl=en&q="+wordnew
    req = request.Request(url ,headers=headers)
    r=request.urlopen(req)
    data=r.read()
    with open(name+".mp3","wb")as code:
        code.write(data)
    print("downloading with urllib")
    

    
    
if __name__ == "__main__":
    print("input the path of your lyrics:")
    ch=input()
    sing(ch)
        
