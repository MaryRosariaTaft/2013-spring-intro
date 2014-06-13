def divisorList(n):
    ans = []
    for item in range(1,n+1):
        if n % item == 0:
            ans = ans + [item]
    return ans

def isPrime(n):
    if len(divisorList(n)) > 2:
        return "No"
    else:
        return "Yes"

def hailstone(n):
    ans = []
    while n != 1:
        ans = ans + [n]
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return ans + [1]

def fibList(n):
    ans = [0]
    count = 1
    while len(ans) < n:
        ans = ans + [count]
        count = count + ans[-2]
    return ans

m = input("Enter an integer: ")
print "Its divisors: ", divisorList(m)
print "Is it prime? ", isPrime(m)
print "Its hailstone sequence: ", hailstone(m)
print "The Fibonacci sequence with that number of items: ", fibList(m)
