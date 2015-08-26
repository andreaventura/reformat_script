<<<<<<< HEAD
'''Takes a text file and move all instances of {...} immediately after the next '.'to run the script from the terminal type: python reformat_script.py PATH_TO_TXT_FILE > NAME_OF_OUTPUT_FILE'''import sysdef joinText(filename):    f=open(filename,'r')    joinedText=''    for line in f.readlines():        joinedText=joinedText+line    return joinedTextdef moveCitations(text):    newText=''    i=0    while i < len(text):        if text[i] == '{' :            citationEnd=i+(text[i:].find('}'))+1            citation=text[i:citationEnd]            i=citationEnd            while i < len(text):                if text[i]=='.':                    newText=newText+text[i]+citation                    i+=1                    break                else:                    newText=newText+text[i]                    i+=1        newText=newText+text[i]        i+=1    return newTextif __name__=='__main__':    text = joinText(sys.argv[1])    print moveCitations(text)
=======
'''
Takes a text file and move all instances of {...} immediately after the next '.'
to run the script from the terminal type: python reformat_script.py PATH_TO_TXT_FILE > NAME_OF_OUTPUT_FILE
'''
import sys
def joinText(filename):
    f=open(filename,'r')
    joinedText=''
    for line in f.readlines():
        joinedText=joinedText+line
    return joinedText

def moveCitations(text):
    newText=''
    i=0
    while i < len(text):
        if text[i] == '{' :
            citationEnd=i+(text[i:].find('}'))+1
            citation=text[i:citationEnd]
            i=citationEnd
            while i < len(text):
                if text[i]=='.':
                    newText=newText+text[i]+citation
                    i+=1
                    break
                else:
                    newText=newText+text[i]
                    i+=1
        newText=newText+text[i]
        i+=1
    return newText

if __name__=='__main__':
    text = joinText(sys.argv[1])
    print moveCitations(text)
>>>>>>> 3ec357eb8c57890aa8ff5c978cf955efd15053e5
