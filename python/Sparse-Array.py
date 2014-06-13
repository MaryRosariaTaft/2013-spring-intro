def sparseDict(L):
   ans = {}
   for i in range(len(L)):
       if L[i] != 0:
           ans[i] = L[i]
   return ans
           
def addSparseDict(d1,d2):
    ans = {}
    for k in d1.keys():
        ans[k] = d1[k]
    for k in d2.keys():
        if ans.has_key(k):
            ans[k] += d2[k]
        else:
            ans[k] = d2[k]
    return ans

def addSparseDict2(d1,d2):
   ans = d1
   for key in d2.keys():
      if key in ans.keys():
         ans[key] = ans[key] + d2[key]
      else:
         ans[key] = d2[key]
   return ans

def dot(d1,d2):
   ans = 0
   for k in d2:
      if k in d1: #if d1.has_key(k): >>> returns True or False
         ans += d1[k] * d2[k]
   return ans

L1 = [0,0,1,0,1,0,0,3]
L2 = [0,2,0,1,5,0,0,1]
d1 = sparseDict(L1)
d2 = sparseDict(L2)
print "Sparse array - L1: ", L1
print "Sparse array - L2: ", L2
print "Dictionary of L1's non-zero indecies and values: ", d1
print "Dictionary of L2's non-zero indecies and values: : ", d2
print "Union of the dictionaries without a side effect: " , addSparseDict(d1,d2)
print "d1: ", d1
print "d2: ", d2
print "Union of the dictionaries with a side effect: " , addSparseDict2(d1,d2)
print "d1: ", d1
print "     *d1 has been manipulated with this code"
print "d2: ", d2
print "Dot product of the manipulated d1 and d2: ", dot(d1,d2)
