# definitions
def happyBirthday(name):
    print "Happy birthday to you"
    print "Happy birthday to you"
    print "Happy birthday dear " + name
    print "Happy birthday to you"

def fullName (first, last):
    print "first name: " + first
    print "last name: " + last

# calling functions

# n = input("enter a name: ") won't accept numerical (or preassigned) values
n = raw_input("enter a name: ")
happyBirthday(n)

f = raw_input("enter your first name: ")
l = raw_input("enter your last name: ")
fullName (f, l)
