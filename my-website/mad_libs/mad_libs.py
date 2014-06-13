#!/usr/bin/python
print 'Content-Type: text/html'
print

import random

def getText(fileName):
    f = open(fileName, 'r')
    ans = f.read().split()
    f.close()
    return ans

def randomPop(list):
    return list.pop(random.randrange(len(list)))

def partition(text,sep):
    if sep in text:
        text = text.split(sep)
        text.insert(1,sep)
    else:
        return [text,'','']
    return text

def join(str,list):
    a = ''
    for each in list:
        a = a + each + str
    return a[:-len(str)]

##def fixed(wordList): #except it isn't fixed yet
##    paragraph = ""
##    for word in wordList:
##        if "NOUN" in word:
##            word = '<font color="green">' + join('',partition(word,"NOUN")) + '</font>'
##        if "VERB" in word:
##            word = '<font color="red">' + join('',partition(word,"VERB")) + '</font>'
##        if "ADJECTIVE" in word:
##            word = '<font color="blue">' + join('',partition(word,"ADJECTIVE")) + '</font>'
##        if "NAME" in word:
##            word = '<font color="orange">' + join('',partition(word,"NAME")) + '</font>'
##        paragraph += word + ' '
##    return paragraph

def original(wordList):
    paragraph = ""
    for word in wordList:
        paragraph += word + ' '
    return paragraph

def madLibs(wordList,nameList,nounList,verbList,adjectiveList):
    temps = {}
    x = ""
    paragraph = ""
    position = 0
    for word in wordList:
        if word[-1] in "1234567890":
            if word in temps:
                temps[word].append(position)
            else:
                temps[word] = [position]
        else:
            if "NOUN" in word:
                wordList[position] = word.replace("NOUN",randomPop(nounList))
            if "VERB" in word:
                wordList[position] = word.replace("VERB",randomPop(verbList))
            if "ADJECTIVE" in word:
                wordList[position] = word.replace("ADJECTIVE",randomPop(adjectiveList))
            if "NAME" in word:
                wordList[position] = word.replace("NAME",randomPop(nameList))
        position += 1
    for key in temps:
        if "NOUN" in key:
            x = randomPop(nounList)
        if "VERB" in key:
            x = randomPop(verbList)
        if "ADJECTIVE" in key:
            x = randomPop(adjectiveList)
        if "NAME" in key:
            x = randomPop(nameList)
        for place in temps[key]:
            wordList[place] = x
    for word in wordList:
        paragraph += word + ' '
    f = open('Mad-Libs.txt','w')
    f.write(paragraph)
    f.close()
    return paragraph


wordList = getText('Story.txt')
nameList = getText('Names.txt')
nounList = getText('Nouns.txt')
verbList = getText('Verbs.txt')
adjectiveList = getText('Adjectives.txt')
 
print '''<html>
            <head><title>Mad Libs</title></head>
            <body>
                Original story (taken from <i> Moby Dick </i> by Herman Melville):
                <p>
      '''

##print original(wordList)

print "The <font color="+'"green"'+">NOUN</font> was darted; the <font color="+'"blue"'+">ADJECTIVE</font> whale flew forward; with igniting <font color="+'"green"'+">NOUN</font> the line <font color="+'"red"'+">VERB</font> through the grooves;--ran foul. <font color="+'"orange"'+">NAME</font> stooped to <font color="+'"red"'+">VERB1</font> it; he did <font color="+'"red"'+">VERB1</font> it; but the <font color="+'"blue"'+">ADJECTIVE</font> turn <font color="+'"red"'+">VERBed</font> him round the neck, and voicelessly as <font color="+'"blue"'+">ADJECTIVE</font> mutes bowstring their <font color="+'"green"'+">NOUN</font>, he was shot out of the <font color="+'"green"'+">NOUN</font>, ere the crew <font color="+'"red"'+">VERBed</font> he was gone. Next instant, the <font color="+'"blue"'+">ADJECTIVE</font> eye-splice in the rope's final <font color="+'"green"'+">NOUN</font> flew out of the stark-empty tub, knocked down <font color="+'"orange"'+">NAME</font>, and smiting the sea, <font color="+'"red"'+">VERBed</font> in its depths."

print '''       <p>
                New story:
                <p>
      '''

print madLibs(wordList,nameList,nounList,verbList,adjectiveList)

print '''       
            </body>
         </html>
      '''
