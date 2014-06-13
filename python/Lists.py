def sumOdds(L):
    ans = 0
    for item in L:
        if item % 2 == 1:
            ans = ans + item
    return ans

def collectOdds(L):
    ans = []
    for item in L:
        if item % 2 == 1:
            ans = ans + [item]
    return ans

list = input("Enter a list of integers: ")
print sumOdds(list)
print collectOdds(list)
