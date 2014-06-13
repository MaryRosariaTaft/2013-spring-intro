import random

def getText(fileName):
    f = open(fileName, 'r')
    ans = f.read().split()
    f.close()
    return ans

def randomPop(list):
    return list.pop(random.randrange(len(list)))

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
    f = open('MadLibs.txt','w')
    f.write(paragraph)
    f.close()
    return paragraph


wordList = getText('story.txt')
nameList = getText('names.txt')
nounList = getText('nouns.txt')
verbList = getText('verbs.txt')
adjectiveList = getText('adjectives.txt')
print "Words from the story: ", wordList
print "Names: ", nameList
print "Nouns: ", nounList
print "Verbs: ", verbList
print "Adjectives: ", adjectiveList
print "New paragraph: ", madLibs(wordList,nameList,nounList,verbList,adjectiveList)
