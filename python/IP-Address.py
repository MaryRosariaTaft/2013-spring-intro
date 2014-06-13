import random

##Only use random.randrange once.
##X.X.X.X
##X [0,255]
def randomIP():
    ans = ""
    count = 4
    while count > 0:
        ans = ans + "." + str(random.randrange(0,256))
        count = count - 1
    return ans[1:]

print randomIP()

##Twice now.
##NXX-NXX-XXXX
##N [2,9]
##X [0,9]
def randomPhoneNumber(): #digit-by-digit
    ans = ""
    count = 12
    while count > 0:
        n = str(random.randrange(2,9))
        x = str(random.randrange(0,9))
        if count == 12 or count == 8:
            ans = ans + n
        elif str(count) in "11023467":
            ans = ans + x
        else:
            ans = ans + "-"
        count = count - 1
    return ans

def randomPhoneNumber1(): #by chunks of digits
    ans = ""
    count = 0
    while count < 3:
        if count == 2:
            ans = ans + ("000" + str(random.randrange(0,10000)))[-4:]
        else:
            ans = ans + str(random.randrange(200,1000))
        count = count + 1
    return ans

print randomPhoneNumber()
print randomPhoneNumber1()
