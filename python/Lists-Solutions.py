##preconditions: n is an integer greater than 0

def listOfOdds(n):
    ans = []
    count = 1
    while count <= n:
        ans = ans + [count]
        count = count + 2
    return ans

def listOfOdds2(n):
    ans = []
    while n > 0:
        if n % 2 == 1:
            ans = [n] + ans
        n = n - 1
    return ans


def listOfOdds(n):
    return range(1,n,2)

def firstNOdds(n):
    ans = []
    count = 1
    while n > 0:
        n = n - 1
        ans = ans + [count]
        count = count + 2
    return ans


def firstNOdds2(n):
    if (n == 0): return []
    ans = [1]
    count = n - 1
    while count > 0:
        ans = ans + [ans[-1] + 2]
        count = count - 1
    return ans

def firstNOdds3(n):
    return listOfOdds(n*2 - 1)

def firstNOdds4(n):
    return range(1,n*2,2)

#uses: firstNOdds(5)[:-2] >>> [7,9]


n = input("Enter a #: ")
print 'list of odd up to', n, listOfOdds(n)
print 'list of odd up to', n, listOfOdds2(n)
print 'first', n, 'odds:', firstNOdds4(n)
