#!/usr/bin/python

f = open('database.csv','r')
data = f.readlines()
f.close()

##indexList = data[0].split(',')

print "Content-Type: text/html\n\n"
print  '''
<html>
    <head> <title> Catalog </title> </head>
         '''

print '''<p> <b> Catalog </b>
         <table><table border="1"><tr>'''

for head in data[0].split(','):
    print '<td><b>' + head + '</b></td>'

print '</tr>'

for line in data[1:]:
    print '<tr>'
    x = line.split(',')
    y = x[:8]
    z = x[8:]
    for each in y:
        print '<td>' + each + '</td>'
    print '<td>'
    while len(z) > 1:
        for each in z:
            print each + ', '
            z.remove(each)
    print z[-1]
    print '</tr>'

print '''</table>
        <p>
        <a href="input.html">Add another book</a>
    </body>
</html>
'''
