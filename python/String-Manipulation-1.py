W = "python"

#yth

print W[1:4]
print W[-5:-2]

#py
print W[:2]
print W[:-4]

#on
print W[4:]
print W[-2:]

#############

S = "apple"

def collectA(word):
    if "a" not in word:
        return ""
    elif word[0] == "a":
        return "a" + collectA(word[1:])
    else:
        return collectA(word[1:])

b = raw_input("Enter a word to return all it's a's, the word without its a's, and the number of a's it has: ")

print collectA(b)

def removeA(word):
    if "a" not in word:
        return word
    elif word[0] == "a":
        return removeA(word[1:])
    else:
        return word[0] + removeA(word[1:])

print removeA(b)

def countA(word):
    if "a" not in word:
        return 0
    elif word[0] == "a": #or word[0] in "Aa"
        return 1 + countA(word[1:])
    else:
        return countA(word[1:])
    #or
    #len(collectA(word))

print countA(b)

def countA1(word):
    ans = 0
    for letter in word:
        if letter in "Aa":
            ans = ans + 1
        return ans

def reverse(word):
    ans = ""
    for letter in word:
        ans = letter + ans
    return ans #make sure this is indented; if it's inside the "for" loop, it will terminate the function

test = raw_input ("scustamad...: ")
print reverse(test)
        
