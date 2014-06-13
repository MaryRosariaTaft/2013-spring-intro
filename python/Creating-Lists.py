#preconditions: n is an integer greater than or equal to one

def listOfOdds(n):
    ans = []
    while n > 0:
        if n % 2 == 1:
            ans = [n] + ans
        n = n - 1
    return ans

def listOfOdds2(n):
    ans = []
    count = 1
    while count <= n:
        ans = ans + [count]
        count = count + 2
    return ans

def firstNOdds(n):
    ans = []
    count = 1
    while len(ans) < n:
        ans = ans + [count]
        count = count + 2
    return ans


def firstNOdds2(n):
    return listOfOdds(n*2-1)

m = input("Enter an integer: ")
print listOfOdds(m)
print firstNOdds(m)
