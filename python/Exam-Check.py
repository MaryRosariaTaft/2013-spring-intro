##comment out all the top stuff!
Part I: Short Answer (25 pts)
======
  Evaluate the following:

   a = 'crab'
   b = 'clams'
   c = 'starfish'

   L1 = [a,b,c] == ['crab', 'clams', 'starfish']
   L2 = L1[-2:] == ['clams', 'starfish']


   a. len(L1 + L2)
5
   b. L1 + L2 * len(b[2:4])
['crab', 'clams', 'starfish', 'clams', 'starfish', 'clams', 'starfish']
   c. L1[::-1] 
['starfish', 'clams', 'crab']
   d. L1[1][2]
'a'
   e. a in L1
True
   f. [a] not in L1
True
   g. 1 < 3 < 5
True
   h. 1 < 3 and 3 < 5
True

Part II:
=======
    Use range() to generate the following lists:

    1. [2,3,4,5,6]
range(2,7)

    2. [6,5,4,3,2]
range(6,1,-1)

    3. [5,8,11,14,17]
range(5,18,3)

    4. A student uses the code
            range(1,10,random.randrange(1,10))
       and gets the list [1,7].

       Then runs the code again and gets [1,9].
       Runs the code again and gets [1,3,5,7,9].

       Explain what is going on.
1st - (1,10,6)
2nd - (1,10,8)
3rd - (1,10,2)


    5. Given this code:
       L = ['at','be','cow','duck','elephant']
       ans = 0
       for n in range(0,len(L),2):
       	   ans = ans + len(L[n])
       return ans

       What is the value of ans?

for n in [0, 2, 4]
0 + 2 + 3 + 8 == 13
       
       	  
      

  

Part III:
========

 Write the lenOfLongestWord(L). Assume L is a list of strings.
 lenOfLongestWord(L) returns the length of the longest word in list L.


  Test Cases:
  lenOfLongestWord(["cat","doggy","pig"]) returns 5
  lenOfLongestWord(["cat","pig"]) returns 3


  def lenOfLongestWord(L):
	ans = ""
	for word in L:
		if len(word) > len(ans):
			ans = word
	return len(ans)





Part IV:
========

 Write localMaxs(L). Assume L is a list of integers. A local max is
 a number which is greater than the number to its left and greater than
 the number to its right. A local max is never at the front or the end
 of a list. The function localMaxs(L) returns a list of all the local
 max's in list L.

 Test Cases:
 localMaxs([]) returns []
 localMaxs([1]) returns []
 localMaxs([1,3,2,6,6,7,4]) returns [3,7]
 localMaxs([1,2,3,4,5]) returns []

def localMaxs(L):
	ans = []
	while len(L) > 3:
		if max(L[0,2]) == L[1]:
			ans = ans + [L[1]]
		L = L[1:]
	return ans


######################


a = 'crab'
b = 'clams'
c = 'starfish'
L1 = [a,b,c]
L2 = L1[-2:]

L = ['at','be','cow','duck','elephant']

def examtest():
    ans = 0
    for n in range(0,len(L),2):
        ans = ans + len(L[n])
    return ans

print examtest()

def lenOfLongestWord(L):
    ans = ""
    for word in L:
        if len(word) > len(ans):
            ans = word
    return len(ans)

def localMaxs(L):
	ans = []
	while len(L) >= 3:
		if L[1] > L[0] and L[1] > L[2]:
			ans = ans + [L[1]]
		L = L[1:]
	return ans
