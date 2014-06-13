#Converts numbers to English words

#precondition : 0 <= n < 1000000
def numToEng(n):
    ans = ""
    if (n < 10):
       ans = digits(n)
    elif (n < 20):
        ans = teens(n)
    elif ( n % 10 == 0 and n < 100):
        ans = tensPrefix(n)
    elif  n < 100:
        ans = tensPrefix(n/10 * 10) + "-" + numToEng(n%10);
    elif n < 1000 and n % 100 == 0:
        ans = digits(n/100) + " hundred "
    elif n < 1000:
        ans = digits(n/100) + " hundred " + numToEng(n%100)
    elif n < 1000000 and n % 1000 == 0:
        ans = numToEng(n/1000) + " thousand "
    elif n < 1000000:
        ans = digits(n/1000) + " thousand " + numToEng(n%1000)
    else:
        ans = "not done yet"
    return ans


#precondition: 0 <= n < 10
def digits(n):
    if (n == 0):
        ans = "zero"
    elif (n == 1):
        ans = "one"
    elif (n == 2):
        ans = "two"
    elif (n == 3):
        ans = "three"
    elif (n == 4):
        ans = "four"
    elif (n == 5):
        ans = "five"
    elif (n == 6):
        ans = "six"
    elif (n == 7):
        ans = "seven"
    elif (n == 8):
        ans = "eight"
    else:
        ans = 'nine'
    return ans

#precondition: 11 <= n < 20
def teens(n):
    if (n == 11):
        ans = "eleven"
    elif (n == 12):
        ans = "twelve"
    elif (n == 13):
        ans = "thirteen"
    elif (n == 14):
        ans = "fourteen"
    elif (n == 15):
        ans = "fifteen"
    elif (n == 16):
        ans = "sixteen"
    elif (n == 17):
        ans = "seventeen"
    elif (n == 18):
        ans = "eighteen"
    else:
        ans = "nineteen"
    return ans

#precondition : 20 <= n <= 90 and n is a multiple of 10
def tensPrefix(n):
    if n == 20:
        ans = "twenty"
    elif n == 30:
        ans = "thirty"
    elif n == 40:
        ans = "forty"
    elif n == 50:
        ans = "fifty"
    elif n == 60:
        ans = "sixty"
    elif n == 70:
        ans = "seventy"
    elif n == 80:
        ans = 'eighty'
    else:
        ans = 'ninety'
    return ans
    




n = input("enter a number less than a million: ")
print numToEng(n)

#Error - Any multiple of 100,000 returns with the words "hundred  thousand" as such, with two spaces between.
