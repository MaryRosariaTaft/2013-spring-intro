##L1 = ['apple','banana','kiwi']
##L2 = ['orange','grape']
##L3 = L1[1:] + [L2[-1]] ## ['banana', 'kiwi', 'grape']
####
##a. L3 * 2 + L1
##>>> ['banana', 'kiwi', 'grape', 'banana', 'kiwi', 'grape', 'apple','banana','kiwi']
##
##b. L2[1][-1]  ##read left to right
##>>> 'e'
##
##c. len(L1+L2+L3)
##>>> 8
##
##d. L1[0] = L2[-1]
##>>> L1 == ['grape', 'banana', 'kiwi']
##
##e. L2[1] = L2
##>>> L2 = ['orange', ['orange', 'grape']]
##
##f. len(L2)
##>>> 2

def upper(L):
    ans = []
    for item in L:
        ans = ans + [str.upper(item)]
    return ans

m = input("Enter a list of words: ")
print upper(m)
