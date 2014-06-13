f = open('Yankees.csv','r')
data = f.readlines()
f.close()
indexList = data[0].split(',') #list of the column headers
#Example: winIndex=indexList.index('W')#W stands for wins
#nextLine = data[1].split(',') #list of the information in the first row

def getSum(columnName):
    ans = 0
    index = indexList.index(columnName)
    for each in data[1:]:
        ans += int(each.split(',')[index])
    return ans

def getAverage(columnName):
    return (getSum(columnName))/(len(data) - 1)

def yearOfMax(columnName): #this will only return one of the top years, if there are more than one
    high = 0
    index = indexList.index(columnName)
    for each in data[1:]:
        if int(each.split(',')[index]) > high:
            high = int(each.split(',')[index])
            year = each.split(',')[1]
    return year

x = raw_input('Column: ')
print "Sum of the column: ", getSum(x)
print "Average of the column: ", getAverage(x)
print "Year of the highest value in that column: ", yearOfMax(x)
print "Percentage won: ", str(100*getSum('W')/getSum('G'))+'%'
print "P.S. Yankees uber alles"
