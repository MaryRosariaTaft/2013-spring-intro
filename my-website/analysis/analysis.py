#!/usr/bin/python
print 'Content-Type: text/html'
print


y = open('Yankees.csv','r')
yData = y.readlines()
y.close()
yIndexList = yData[0].split(',')

g = open('Giants.csv','r')
gData = g.readlines()
g.close()
gIndexList = gData[0].split(',')


def getSum(columnName,indexList,data):
    ans = 0
    index = indexList.index(columnName)
    for each in data[1:]:
        ans += int(each.split(',')[index])
    return ans

def getAverage(columnName,indexList,data):
    return (getSum(columnName,indexList,data))/(len(data) - 1)

def columnMax(columnName,indexList,data):
    ans = 0
    index = indexList.index(columnName)
    for each in data[1:]:
        if int(each.split(',')[index]) > ans:
            ans = int(each.split(',')[index])
    return ans

def columnMin(columnName,indexList,data):
    ans = columnMax(columnName,indexList,data)
    index = indexList.index(columnName)
    for each in data[1:]:
        if int(each.split(',')[index]) < ans:
            ans = int(each.split(',')[index])
    return ans

def yearOfMax(columnName,indexList,data):
    high = 0
    years = []
    index = indexList.index(columnName)
    for each in data[1:]:
        if int(each.split(',')[index]) == high:
            years.append(each.split(',')[1]) 
        if int(each.split(',')[index]) > high:
            high = int(each.split(',')[index])
            years = [each.split(',')[1]]
    return years

def yearOfMax1(columnName,indexList,data):
    high = 0
    years = []
    index = indexList.index(columnName)
    for each in data[1:]:
        if int(each.split(',')[index]) == high:
            years.append(each.split(',')[0]) 
        if int(each.split(',')[index]) > high:
            high = int(each.split(',')[index])
            years = [each.split(',')[0]]
    return years


##print "Average wins: ", str(100*getSum('W',yIndexList,yData)/getSum('G',yIndexList,yData))+'%'
##print "Most wins: ", columnMax('W',yIndexList,yData)
##print "Year of most wins: ", yearOfMax('W',yIndexList,yData)
##print "Most losses: ", columnMax('L',yIndexList,yData)
##print "Year of most losses: ", yearOfMax('L',yIndexList,yData)
##print "Total number of ties: ", getSum('Ties',yIndexList,yData)
##
##print "Average wins: ", str(100*getSum('W',gIndexList,gData)/(getSum('W',gIndexList,gData)+getSum('L',gIndexList,gData)+getSum('T',gIndexList,gData)))+'%'
##print "Most wins: ", columnMax('W',gIndexList,gData)
##print "Year of most wins: ", yearOfMax1('W',gIndexList,gData)
##print "Most losses: ", columnMax('L',gIndexList,gData)
##print "Year of most losses: ", yearOfMax1('L',gIndexList,gData)
##print "Total number of ties: ", getSum('T',gIndexList,gData)

print '''<html>
            <head><title>Data Analysis</title></head>
            <body> '''
print "This data covers ", 1 + columnMax('Year',yIndexList,yData) - columnMin('Year',yIndexList,yData), "years for the Yankees (", columnMin('Year',yIndexList,yData), "through", columnMax('Year',yIndexList,yData), ") and",
print 1 + columnMax('Year',gIndexList,gData) - columnMin('Year',gIndexList,gData), "years for the Giants (", columnMin('Year',gIndexList,gData), "through", columnMax('Year',gIndexList,gData), ")."
print "<ul> <b> The Yankees </b>"
print "<li>The Yankees have an average winning percentage of ", str(100*getSum('W',yIndexList,yData)/getSum('G',yIndexList,yData)), "%.</li>"
print "<li>They won ", str(columnMax('W',yIndexList,yData)), "games, their best yet, in "
for each in yearOfMax('W',yIndexList,yData):
    print each
print ".</li>"
print "<li>They lost ", str(columnMax('L',yIndexList,yData)), "games, their worst in history, in "
for each in yearOfMax('L',yIndexList,yData):
    print each
print ".</li>"
print "<li>Since the formation of the team, ", str(getSum('Ties',yIndexList,yData)), "of their games have resulted in ties, an average of", 93./113, "ties per year.</li>"

print '</ul> <ul> <b>The Giants</b>'
print "<li>The Giants ar just trailing the Yankees, with an average winning percentage of ", str(100*getSum('W',gIndexList,gData)/(getSum('W',gIndexList,gData)+getSum('L',gIndexList,gData)+getSum('T',gIndexList,gData))), "%.</li>"
print "<li>They won their most games in", 
for each in yearOfMax1('W',gIndexList,gData):
    print each
print "with", str(columnMax('W',gIndexList,gData)), "wins.</li>"
print "<li>However, they lost a disappointing", str(columnMax('L',gIndexList,gData)), "games in (brace yourself)",
x = yearOfMax1('L',gIndexList,gData)
x.reverse()
for each in x:
    if each != x[-1]:
        print each, ","
    else:
        print "<b>and</b> ", each, ".  (Let's hope that list doesn't get any longer.)</li>"
print "<li>", str(getSum('T',gIndexList,gData)), "of their games were ties, an average of ", 33./88, "per year.</li></ul><p>"
print '''Note the average ties per year: even though baseball games technically don't end in ties - they go into extra innings - the Yankees have had many more tie games than the Giants.  Even considering they play many-fold more games per year, it "shouldn't" have happened, but it did.
        It is especially surprising to my generation, because in the last 30 years (as displayed) there were only 3 tie games.  However, if you look at the <a href="data.py">data</a>, a couple of tie games per year used to be relatively common.<br>
        Hope you enjoyed the statistics!  If you'd like me to generate some more, e-mail me at Mary.Taft97@gmail.com, and I'll try them out.
            <p><a href="data.py"> <small> Data used to derive these statistics </small> </a>
            </body>
         </html>
      '''

