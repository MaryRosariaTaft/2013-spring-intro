def makeSet(L):
    ans = []
    for item in L:
        if item not in ans:
            ans.append(item)
    return ans

##def reverseDict(d):
##    ans = {}
##    for value in d:
##        if d[value] not in ans.keys():
##            ans[d[value]] = [value]
##        else:
##            ans[d[each]].append(each)
##    return ans

def sparseDict(L):
    ans = {}
    position = 0
    for item in L:
        if item != 0:
            ans[position] = item
        position = position + 1
##    for i in range(len(L)):
##        if L[i] != 0:
##            ans [i] = L[i]
    return ans

def sparseDict2(L):
    ans = {}
    while len(L) > 0:
        if L[-1] != 0:
            ans[len(L)-1] = L[-1]
        L = L[:-1]
    return ans

def addsparseDict(L1,L2):
##    a = sparseDict(L1)
##    b = sparseDict(L2)
    for key in L1:
        if key not in L1:
            L1[key] = L2[key]
        else:
            L1[key] = (L1[key] + L2[key])
    return L1

                
##d = input("Enter a dictioanry: ")
##L = input("Enter a list: ")
##print "Placement of non-zero values: ", sparseDict(L)
##print "And with a different code: ", sparseDict2(L)
print "Compacted: ", addsparseDict(sparseDict(L1),sparseDict(L2))
