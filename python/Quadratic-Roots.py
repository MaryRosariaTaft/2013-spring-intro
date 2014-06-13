#definitions

#precondition: b*b - 4*a*c > 0
def quad_solver(a, b, c):
    print "root 1: " , (-b + (b**2 - 4.*a*c) ** (1./2)) / (2.*a)
    print "root 2: " , (-b - (b**2 - 4.*a*c) ** (1./2)) / (2.*a)

#calling
q = input("Enter quadratic coefficient: ")
l = input("Enter linear coefficient: ")
t = input("Enter constant: ")
quad_solver(q, l, t)
