'''
Takes a text file and move all instances of {...} immediately after the next '.'
to run the script from the terminal type: python reformat_script.py PATH_TO_TXT_FILE > NAME_OF_OUTPUT_FILE
'''
import sys, re

def joinText(filename):
    f=open(filename,'r')
    joinedText=''
    for line in f.readlines():
        joinedText=joinedText+line
    return joinedText

def moveCitations(text):
    periods=text.split('.')
    newText=''
    for period in periods:
        period = period + '.' #add the dot back!
        #get all citations starts in decreasing order (from last to first)
        citations=re.finditer('{[^}]*}', period) #finds every occurrence of {...} in the period.
        spans =[]
        for citation in citations: #copies the citation at the end of the period
            period=period+citation.group()
            spans.append(citation.span())
        for span in reversed(spans): #deletes the citation from the body of the period.
            if period[span[0]-1]==' ': #this ensures that if the {...} is preceded by a space, the space is removed from the edited text. Thus "text {citation} text."  is reformatted to "text text.{citation}" and not "text  text.{citation}"
                span=list(span) #because tuples do not support list assignment
                span[0]-=1
            period=period[:span[0]]+period[span[1]:]
        newText=newText+period
    return newText



if __name__=='__main__':
    text = joinText(sys.argv[1])
    formatted_text=moveCitations(text)
    if len(sys.argv) > 2:
        out_file=sys.argv[2]
        f=open(out_file, 'w')
        f.write(formatted_text)
        f.close()
    else:
        print formatted_text
