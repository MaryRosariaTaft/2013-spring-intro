def odd(n):
    return n%2 == 1

def even(n):
    return n%2 == 0

def oddDigits_forloop(n):
    ans = ""
    n = `n`
    for digit in n:
        if digit in "13579":
            ans = ans + digit
        if len(ans) == 0:
            ans = "-1"
    return int(ans)

def oddDigits_whileloop(n):
    ans = ""
    n = `n`
    while len(n) > 0:
        if n[0] in "13579":
            ans = ans + n[0]
        n = n[1:]
    return int(ans)


def oddDigits_recursive(n): #doesn't work yet
    ans = ""
    n = `n`
    if n[0] in "13579":
        ans = ans + n[0]
    if len(n) > 1:
        oddDigits_recursive(int(n[1:]))
    if len(n) == 1:
        if n[0] in "13579":
            ans = ans + n
    return ans


temp = input("Enter a number: ")
print oddDigits_forloop(temp)
print oddDigits_whileloop(temp)
print oddDigits_recursive(temp)

###########################

a = 2
b = 3.7
c = float(a)
d = int(b)
e = str(a) + str(b) + str(c) + str(d)

print c == 2.0
print d == 3
print e == "23.72.03"
