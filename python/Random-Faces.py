import random

def newface():
    print "  |||||||||||||||||  "
    print "  |               |  "
    print "  |   o       o   |  "
    print " _|               |_ "
    print "|_                 _|"
    print "  |   |-------|   |  "
    print "  |               |  "
    

def hair():
    print "  " + 17 * "|" + "  "
def bald():
    print "   " + 15 * "_"
def parted():
    print "   " + 2*(7*"_" + " ")
def randomhair():
    randnum = random.randint(1,3)
    if randnum == 1:
        bald()
    elif randnum == 2:
        parted()
    else:
        hair()
        

def sides():
    print "  |" + 15 * " " + "|  "


def eyes():
    print "  |   o       o   |  "
def tiredeyes():
    print "  |   _       _   |  "
def openeyes():
    print "  |   0       0   |  "
def randomeyes():
    randnum = random.randint(1,3)
    if randnum == 1:
        eyes()
    elif randnum == 2:
        tiredeyes()
    else:
        openeyes()
    

def bignose():
    print " _|" + 15 * " " + "|_ "
    print "|_       (__)      _|"
def smallnose():
    print " _|" + 15 * " " + "|_ "
    print "|_        ..       _|"
def nonose():
    print " _|" + 15 * " " + "|_ "
    print "|_" + 17 * " " + "_|"
def randomnose():
    randnum = random.randint(1,3)
    if randnum == 1:
        bignose()
    elif randnum == 2:
        smallnose()
    else:
        nonose()


def mouth():
    print "  |   |_______|   |  "
def upsetmouth():
    print "  |   |-------|   |  "
def teethmouth():
    print "  |   |_|_|_|_|   |  "
def randommouth():
    randnum = random.randint(1,3)
    if randnum == 1:
        mouth()
    elif randnum == 2:
        upsetmouth()
    else:
        teethmouth()

def randomface():
    randomhair()
    sides()
    randomeyes()
    randomnose()
    randommouth()
    sides()
