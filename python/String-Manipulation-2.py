def reverse(word):
    ans = ""
    for letter in word:
        ans = letter + ans
    return ans

def isPalindrome(word):
    if word == reverse(word):
        return "true"
    else:
        return "false"
	#or
	#return reverse(word) == word

def collectVowels(word):
    ans = ""
    for letter in word:
        if letter in "aeiou":
            ans = ans + letter
    return ans

test = raw_input("Enter a word: ")
print "'", reverse(test), "' is the reverse of this word."
print "It is ", isPalindrome(test), " that this is a palindrome."
print "This word's vowels are '", collectVowels(test), "'"
