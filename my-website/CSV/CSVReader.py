f = open('Baseball.csv', 'r')
x = f.readlines()
f.close()

print x
print 'Heading: ', x[0]
print 'Teams: '
for line in x[1:]:
    print line.split(', ')[0]
