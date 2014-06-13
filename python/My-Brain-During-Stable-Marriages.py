##a - xyz; b - xzy; c - zxy
##x - abc; y - bca; z - bca

##Generate Marriages 1
##Round 1: ax, bx, cz
##    x rejects b
##Round 2: bz
##    z rejects c
##Round 3: cx
##    x rejects c
##Round 4: cy
##Final: ax, bz, cy

##Each man proposes to his first choice.
##Each woman accepts only one offer.
##Each rejected man proposes to his second choice.
##Each woman accepts only one offer.
##Each rejected man proposes to his third choice.
##Each woman accepts only one offer.
##Etc., etc., ad nauseum.
##Stop when no more men have been rejected.

##Each man proposes.
##Couples are formed.
##Each woman who received a proposal accepts one.
##She rejects the others.*
##Couples are edited, deleting the rejected pairs.
##Each rejected man proposes to his next choice.
##Repeat.
##Stop when no more men have been rejected.
##
##* Go through each partner.
##  If he is not the most desirable she's encountered, reject him.

menPrefs = {
 'abe':{1:'sally',2:'mary',3:'cindy'},
 'greg':{1:'sally',2:'mary',3:'cindy'},
 'max':{1:'cindy',2:'mary',3:'sally'}
}

womenPrefs = {
 'sally':{1:'greg',2:'abe',3:'max'},
 'mary':{1:'greg',2:'max',3:'abe'},
 'cindy':{1:'max',2:'greg',3:'abe'}
}

def reverseDict(d):
    ans = {}
    for key in d.keys():
        if d[key] not in ans.keys():
            ans[d[key]] = key
        else:
            ans[d[key]] = ans[d[key]] + key
    return ans

##reverseDict(womenPrefs[sally]) = {'greg':1,'abe':2,'max':3}
##{'greg':1,'abe':2,'max':3}['greg'] == 1
##reverseDict(womenPrefs[sally])['greg'] == 1

def generateMarriages(menPrefs,womenPrefs):
    couples = {}
    singleMen = menPrefs.keys()
    currentChoice = len(menPrefs)
    round = 1
    while len(singleMen) > 0:
        for man in menPrefs:
            couples[man] = menPrefs[man][round]
            couples[menPrefs[man][round]] = man
        for woman in womenPrefs:
            if woman in couples:
                if len(couples[woman]) > 0:
                    while len(couples[woman]) > 0:
                        for man in couples[woman]:
##                            if currentChoice > reverseDict(womenPrefs[woman])[man]:
##                                del couples[man]
        for man in menPrefs:
            if man in couples:
                singleMen = singleMen[:man] + singleMen[man+1:]
        #currentChoice = len{menPrefs)
        round += 1
    return couples

print generateMarriages(menPrefs,womenPrefs)

##def generateMarriages(menPrefs,womenPrefs):
##    men = {}
##    women = {}
##    singleMen = menPrefs.keys()
##    top = len(menPerfs)
##    while len(singleMen) > 0:
##        for man in menPrefs:
##            men[man] = menPrefs[man][1]
##            women[menPrefs[man][1]] = man
##        for woman in women:
##            if len(women[woman]) > 1:
##                for offer in women[woman]:
##                    if ###the pref number of that man < top:
##                        top = ###that pref number
                    

##Generate Marriages 2
##Round 1: ax
##    b - zy; c - zy
##    y - bc; z - bc
##Round 2: bz
##    c - z
##    z - c
##Round 3 - cy
##Final: ax, bz, cy


##def generateMarriages(menPrefs,womenPrefs):
##    marriages = {}
##    rd = 1
##    while #######:
##        for man in menPrefs:
##            marriages[man] = menPrefs[man][rd]
##            marriages[menPrefs[man][rd]] = man
##        for women in womenPerfs:
##            if marriages[woman] == womenPerfs[woman]
        

##def generateMarriages2(menPrefs,womenPrefs):
##    marriages = {}
##    while len(menPrefs) > 0:
##        for man in menPrefs:
##            if man == womenPrefs[menPrefs[man][min(menPrefs[man])]][min(womenPrefs[menPrefs[man][min(menPrefs[man])]])]:
##                marriages[man] = menPrefs[man][min(menPrefs[man])]
##                marriages[menPrefs[man][min(menPrefs[man])]] = man
##                del menPerfs[man]
##                for woman in womenPerfs:
##                    del womenPerfs[woman][man]
