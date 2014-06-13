##def factorial(n):
##    ans = 1
##    while n > 0:
##        ans = ans * n
##        n = n - 1 #update - necessary for boolean to eventually become false
##    return ans
##
##temp = input("Enter a number for its factorial value: ")
##print factorial(temp)
##
##
##def numDigits(n):
##    ans = 1
##    while n > 0:
##        ans = ans + 1
##        n = n / 10
##    return ans - 1
##
##temp1 = input("Enter a number for its number of digits: ")
##print numDigits(temp1)
##
##
##def sumDigits(n):
##    ans = 0
##    while n > 0:
##        ans = ans + n%10
##        n = n/10
##    return ans
##
##temp2 = input("Enter a number for the sum of its digits: ")
##print sumDigits(temp2)
##
##
##def maxDigit(n):
##    ans = 0
##    while n > 0 and ans != 9:
##        if n%10 > ans:
##            ans = n%10
####or    ans = max(n%10, ans)
##        n = n/10
##    return ans
##
##
##temp3 = input("Enter a number for its highest-value digit: ")
##print maxDigit(temp3)


def commas(n):
    ans = ""
    while n > 999:
        ans = "," + `(n%1000)`+ ans
        n = n / 1000
    return `n` + ans

##def commas(n):
##	ans = ""
##	n = str(n)
##	while len(n) > 3
##		ans = "," + a[-3:] + ans
##		n = n[-3:]
##	return n + ans

temp4 = input("Enter a number to add commas to it: ")
print commas(temp4)
