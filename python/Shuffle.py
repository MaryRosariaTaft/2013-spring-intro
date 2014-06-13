##shuffle(3) --> 3
##shuffle(35) --> 35 or 53
##shuffle(123) --> 123 or 132 or 213 or 231 or 312 or 321

import random

##preconditions: n in an integer without leading zeros --> Python won't interpret it as base 10

def shuffle(n):
    n = `n`
    ans = ""
    while len(n) > 0:
        temp = random.randrange(0,len(n))
        ans = ans + n[temp]
        n = n[:temp] + n[1+temp:]
    return ans

m = input("Enter a number: ")
print shuffle(m)

##def shuffle(n):
##    ans = ""
##    for number in str(n)
##        ans = 
