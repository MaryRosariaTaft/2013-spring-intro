#Stable Marriage Project
#Mary Taft
#Mr. Platek, Period 8
#Completed April 20, 2013

def revD(d):
    ans = {}
    for k in d:
        ans[d[k]] = k
    return ans

def generateMarriages(menPrefs,womenPrefs):
    marriages = {}
    while len(marriages) != len(menPrefs):
        for man in menPrefs:
            if man not in marriages:
                t = 1
                while menPrefs[man][t] in marriages.values() and revD(womenPrefs[menPrefs[man][t]])[man] > revD(womenPrefs[menPrefs[man][t]])[revD(marriages)[menPrefs[man][t]]]: #the man's top preference is already married, and she prefers her current fiance
                    t+= 1
                if menPrefs[man][t] in marriages.values() and revD(womenPrefs[menPrefs[man][t]])[man] < revD(womenPrefs[menPrefs[man][t]])[revD(marriages)[menPrefs[man][t]]]:#this time, she prefers the new offer
                    del marriages[revD(marriages)[menPrefs[man][t]]]
                marriages[man] = menPrefs[man][t]
    marriages.update(revD(marriages))
    return marriages


menPref = {"John" : {1: "Mary", 2: "Cindy"},
             "Bill" : {1: "Mary", 2: "Cindy"}}
womenPref = {"Mary" : {1: "John", 2: "Bill"},
 	       "Cindy" : {1: "Bill", 2: "John"}}

m = {'a':{1:'x',2:'y',3:'z'},
     'b':{1:'x',2:'z',3:'y'},
     'c':{1:'z',2:'x',3:'y'}}
w = {'x':{1:'a',2:'b',3:'c'},
     'y':{1:'b',2:'c',3:'a'},
     'z':{1:'b',2:'c',3:'a'}}

menPrefs = {'Abe':{1:'Sally',2:'Mary',3:'Cindy'},
            'Greg':{1:'Sally',2:'Mary',3:'Cindy'},
            'Max':{1:'Cindy',2:'Mary',3:'Sally'}}
womenPrefs = {'Sally':{1:'Greg',2:'Abe',3:'Max'},
              'Mary':{1:'Greg',2:'Max',3:'Abe'},
              'Cindy':{1:'Max',2:'Greg',3:'Abe'}}

men = {'a':{1:'z',2:'w',3:'y',4:'x',5:'v',6:'u'},
       'b':{1:'u',2:'y',3:'z',4:'v',5:'w',6:'x'},
       'c':{1:'y',2:'w',3:'x',4:'z',5:'u',6:'v'},
       'd':{1:'x',2:'y',3:'u',4:'w',5:'v',6:'z'},
       'e':{1:'w',2:'u',3:'z',4:'y',5:'x',6:'v'},
       'f':{1:'u',2:'z',3:'w',4:'v',5:'y',6:'x'}}
women = {'u':{1:'a',2:'b',3:'c',4:'e',5:'d',6:'f'},
         'v':{1:'b',2:'f',3:'e',4:'a',5:'c',6:'d'},
         'w':{1:'b',2:'a',3:'e',4:'c',5:'f',6:'d'},
         'x':{1:'b',2:'d',3:'c',4:'e',5:'a',6:'f'},
         'y':{1:'d',2:'c',3:'e',4:'f',5:'b',6:'a'},
         'z':{1:'c',2:'e',3:'b',4:'d',5:'a',6:'f'}}

print "Stable Marriage Generator Test Cases", "\n"
print "Two men and two women:", generateMarriages(menPref,womenPref), "\n"
print "Three men and three women: ", generateMarriages(m,w), "\n"
print "A different arrangement of three men and three women: ", generateMarriages(menPrefs,womenPrefs), "\n"
print "Six men and six women: ", generateMarriages(men,women)
