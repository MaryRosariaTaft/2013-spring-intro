def isaVowel(letter):
    return letter in "aeiouAEIOU"

def beginswithVowel(word):
    return isaVowel(word[0])

V = ("a", "e", "i", "o", "u")

def pigLatin(word):
    hold = "ay"
    if beginswithVowel(word):
        return word + "way"
    else:
        for letter in word:
            if letter not in V:
                hold = letter + hold
            else:
                return ### + hold


test = raw_input("Enter a word: ")
print pigLatin(test)

#word[word.find("a"):] + word[0:word.find("a")] + "ay"
