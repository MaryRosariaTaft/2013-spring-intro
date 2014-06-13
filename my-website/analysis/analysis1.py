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
##
##def columnMax(columnName,indexList,data):
##    ans = 0
##    index = indexList.index(columnName)
##    for each in data[1:]:
##        if int(each.split(',')[index]) > ans:
##            ans = int(each.split(',')[index])
##    return ans

def getSum(columnName,indexList,data):
    ans = 0
    index = indexList.index(columnName)
    for each in data[1:]:
        ans += int(each.split(',')[index])
    return ans

def getAverage(columnName,data):
    return (getSum(columnName))/(len(data) - 1)

def columnMax(columnName,indexList,data):
    ans = 0
    index = indexList.index(columnName)
    for each in data[1:]:
        if int(each.split(',')[index]) > ans:
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

def columnMin(columnName,indexList,data):
    ans = 0
    index = indexList.index(columnName)
    for each in data[1:]:
        if int(each.split(',')[index]) < ans:
            ans = int(each.split(',')[index])
    return ans

def yearOfMin(columnName,indexList,data):
    index = indexList.index(columnName)
    low = data[1:][1].split(',')[index]
    for each in data[1:]:
        if int(each.split(',')[index]) < low:
            high = int(each.split(',')[index])
            year = each.split(',')[1]
    return year

print '''<html>
            <head><title>Data Analysis</title></head>
            <body>
                <ul> <b> The Yankees </b>
      '''

temp = yearOfMax('W',yIndexList,yData)
print '<li> In '
if len(temp) > 1:
    while len(temp) > 1:
        print temp.pop(), ', '
    print 'and '
print temp[0], ', the Yankees won ', columnMax('W',yIndexList,yData), ' games.</li>'

temp1 = yearOfMin('L',yIndexList,yData)
print '<li> In '
if len(temp1) > 1:
    while len(temp1) > 1:
        print temp1.pop(), ', '
    print 'and '
print temp1[0], ', the Yankees lost ', columnMax('L',yIndexList,yData), ' games.</li>'

print ''' </ul>
          <ul> Giants '''

temp2 = yearOfMax1('W',gIndexList,gData)
print '<li> In '
if len(temp2) > 1:
    while len(temp2) > 1:
        print temp2.pop(), ', '
    print 'and '
print temp2[0], ', the Giants won ', columnMax('W',gIndexList,gData), ' games.</li>'

temp3 = yearOfMin1('L',gIndexList,gData)
print '<li> In '
if len(temp3) > 1:
    while len(temp3) > 1:
        print temp3.pop(), ', '
    print 'and '
print temp3[0], ', the Giants lost ', columnMax('L',gIndexList,gData), ' games.</li></ul>'

print '''<a href="data.py"> <small> Data used to derive these statistics </small> </a>'''

print '''       
            </body>
         </html>
      '''
