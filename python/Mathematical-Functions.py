import math

def f(x):
    return x + 2

def g(x):
    return 2 * x

def h(x):
    return g(f(x))

n = input("Enter a # to run functions: ")
print "f(",n,")",f(n)
print "g(",n,")",g(n)
print "h(",n,")",h(n)

#####

def myabs(x):
    if x >= 0:
        print x
    else:
        print -x
# or
# print abs(x)
m = input("Enter a # for its absolute value: ")
myabs(m)

#####

def mymax2(x,y):
    if x > y:
        print x
    else:
        print y

num = input("For the larger of two numbers, enter first number: ")
num2 = input("And second number: ")
mymax2 (num, num2)

#####

#pi here = 3.14
#or math.pi
def circleArea(r):
    print 3.14 * r**2
rad = input("Enter a circle's radius for its area: ")
circleArea(rad)

#####

def mymax3(x,y,z):
    if x >= y and x >= z:
        print x
    elif y >= z:
        print y
    else:
        print z
xx = input("For the largest of three numbers, enter the first: ")
yy = input("The second: ")
zz = input("And the third: ")
mymax3(xx,yy,zz)

##def mymax3(x,y,z):
##    print mymax2(mymax2(x,y),z)
##
##def mymax3(x,y,z):
##    print max(x,y,z)

#####

def circleAreahelper(r):
    return 2 * r * 3.14
def annulusArea(r1,r2):
    print circleAreahelper(r1) - circleAreahelper(r2)
rad1 = input("For an annulus's area, enter radius of the larger circle: ")
rad2 = input("And that of the smaller: ")
annulusArea(rad1,rad2)
