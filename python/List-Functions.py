import random

def makeList(a,b,c): #length, low, high
    ans = []
    while a > 0:
        ans.append(random.randrange(b,c))
        a = a - 1
    ans.sort()
    return ans

#min(List) >>> list's minimum #
#max(List) >>> ditto

##def mean(L):
##    temp = 0.0
##    for item in L:
##        temp = temp + item
##    return temp / len(L)

def efficientmean(L):
    return float(sum(L)) / len(L)


##def median(L):
##    L.sort()
##    if len(L) % 2 == 0:
##        return mean([L[len(L)/2],L[-1+len(L)/2]])
##    else:
##        return L[len(L)/2]

def cleanermedian(L):
    L.sort()
    while len(L) > 2:
        L = L[1:-1]
    return mean(L)

def freq(num,L):
    ans = 0
    for item in L:
        if item == num:
            ans = ans + 1
    return ans

def makeSet(L):
    ans = []
    for item in L:
        if item not in ans:
            ans.append(item)
    return ans

def printHistogram(L):
    for item in makeSet(L):
        print item, "|" + "*" * freq(item,L)
    
def localModes(L):
    ans = []
    W = makeSet(L)
    while len(W) >= 3:
        if freq(W[1],L) > freq(W[0],L) and freq(W[1],L) > freq(W[2],L):
            ans.append(W[1])
        W = W[1:]
    return ans

def freqDict(L):
    ans = {}
    for item in L:
        ans[item] = freq(item,L)
    return ans

def modes(dic):
    ans = []
    high = 0
    for f in dic:
        if dic[f] > high:
            ans = [f]
            high = dic[f]
        elif dic[f] == high:
            ans.append(f)
    return ans

a = input("Enter a length: ")
b,c = input("Enter a range: ")
L = makeList(a,b,c)
print "List: ", L
##print mean(L)
print "List's mean: ", efficientmean(L)
##print median(L)
print "List's median: ", cleanermedian(L)
x = input("Enter a number to search for it: ")
print "Its frequency: ", freq(x,L)
print "Set without repeats: ", makeSet(L)
print "Histogram: "
printHistogram(L)
print "Local modes: ", localModes(L)
print "Dictionary of frequencies: ", freqDict(L)
print "Mode(s): ", modes(freqDict(L))
