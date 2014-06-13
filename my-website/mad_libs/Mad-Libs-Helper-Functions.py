import random

def getText(fileName):
    f = open(fileName, 'r')
    ans = f.read().split()
    f.close()
    return ans

def getRandom(list):
    return list[random.randrange(len(list))]

def randomPop(list):
    return list.pop(random.randrange(len(list)))

def replace(text,old,new,n):
    while n > 0:
        x = text.find(old)
        text = text[:x] + new + text[x+len(old):]
        n -= 1
    return text

def replace1(text,old,new,n):
    return text.replace(old,new,n)

def partition(text,sep):
    spot = text.find(sep)
    if sep in text:
        return [text[:spot],sep,text[spot+len(sep):]]
    else:
        return [text,'','']

def partition1(text,sep):
    if sep in text:
        text = text.split(sep)
        text.insert(1,sep)
    else:
        return [text,'','']
    return text

def join(str,list): #changes original list
    x = len(list)
    y = 1
    ans = ''
    while x > 1:
        list.insert(y,str)
        x-=1
        y+=2
    for item in list:
        ans+=item
    return ans

#pre: len(list) > 1
def join1(str,list): #destroys original list
    ans = ''
    while len(list) > 1:
        ans = ans + list.pop(0) + str
    ans = ans + list[0]
    return ans

def join2(str,list): #maintains original list
    a = ''
    for each in list:
        a = a + each + str
    return a[:-len(str)]
