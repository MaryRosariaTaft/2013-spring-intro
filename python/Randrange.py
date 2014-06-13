import random

x = '123456789'

print x[::2] #13579
print x[1::2] #2468
print x[-3:-8:-2] #or x[6:1:-2] #753

#random.randrange(3,5) returns a random integer between 3 and 5, including 3 but not 5.
#3 or 4

#random.randrange(1,10,2) returns a random integer between 1 and 10, including 1 but not 10, and only with intervals of 2 between.
#1, 3, 5, 7, or 9

#random.randrange(10,1,-3) returns a random integer between 10 and 1, including 10 but not 1, and only with intervals of 3 between.
#10, 7, or 4

def randomDigit(n):
    n = `n`
    return int(n[random.randrange(0,len(n))])

m = input("Enter a number: ")
print randomDigit(m)
