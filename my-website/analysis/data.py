#!/usr/bin/python
print 'Content-Type: text/html'
print

## indexList = data[0].split(',')

y = open('Yankees.csv', 'r')
yData = y.readlines()
y.close()

g = open('Giants.csv', 'r')
gData = g.readlines()
g.close()


print '''<html>
            <head><title>Data Analysis</title></head>
            <body>
                I'm proud to say I was born and raised a fan of the New York Yankees and New York Giants.  
                (Good luck trying to convert me.)  
                Thanks to the wonders of computer technology,
                I now have the power to display and analyze their statistics with a few strokes of the keyboard.  
                The following is the franchise data for the two teams.
                <br><small> *Follow the link at the bottom of this page for derived statistics. </small>
      '''

print '''<p> <b> New York Yankees </b> <small><i> Source: http://www.baseball-reference.com/teams/NYY/ </i></small>
         <table><table border="1"><tr>'''

for head in yData[0].split(','):
    print ''' <td><b>''' + head + '''</b></td>'''

print '''</tr>'''

for line in yData[1:]:
    print '''<tr>'''
    x = line.split(',')
    for each in x:
        print '''<td>''' + each + '''</td>'''
    print '''</tr>'''

print '''</table>'''

print '''<p> <b> New York Giants </b> <small><i> Source: http://www.pro-football-reference.com/teams/NYG/ </i></small>
         <table><table border="1"><tr>'''

for head in gData[0].split(','):
    print ''' <td><b>''' + head + '''</b></td>'''

print '''</tr>'''

for line in gData[1:]:
    print '''<tr>'''
    x = line.split(',')
    for each in x:
        print '''<td>''' + each + '''</td>'''
    print '''</tr>'''

print '''</table>'''

print '''<p>
         <a href="analysis.py"> <small> Derived statistics from this data </small> </a>'''

print '''       
            </body>
         </html>
      '''
